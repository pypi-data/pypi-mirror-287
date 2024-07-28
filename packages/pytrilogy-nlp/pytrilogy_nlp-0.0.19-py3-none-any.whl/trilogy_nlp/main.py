import uuid
from typing import List, Union
from trilogy.core.enums import BooleanOperator, Purpose
from trilogy.core.query_processor import process_query
from trilogy.core.models import (
    Comparison,
    Concept,
    Conditional,
    DataType,
    Environment,
    OrderBy,
    Ordering,
    OrderItem,
    SelectStatement,
    WhereClause,
    ProcessedQuery,
    unique,
)

from trilogy_nlp.constants import DEFAULT_LIMIT, logger
from trilogy_nlp.models import (
    FilterResult,
    FinalFilterResult,
    FinalOrderResult,
    InitialParseResponse,
    IntermediateParseResults,
    OrderResult,
    # TokenInputs,
    SemanticTokenResponse,
    FinalParseResponse,
)
from trilogy_nlp.prompts import (
    FilterRefinementCase,
    FilterRefinementErrorCase,
    SelectionPromptCase,
    SemanticExtractionPromptCase,
    SemanticToTokensPromptCase,
    run_prompt,
)
from trilogy_nlp.tokenization import build_token_list_by_purpose, tokens_to_concept
from langchain_core.language_models import BaseLanguageModel
from uuid import UUID


def get_phrase_from_x(x: Union[str, FilterResult, OrderResult]):
    if isinstance(x, str):
        return x
    elif isinstance(x, FilterResult):
        if len(x.values) == 1:
            return f"{x.concept} {x.values[0]}"
        return f"{x.concept} {x.values}"
    elif isinstance(x, OrderResult):
        return x.concept
    raise ValueError


def tokenize_phrases(
    purpose: str,
    phrase_list: List[str],
    tokens: List[str],
    session_uuid,
    log_info: bool,
    llm: BaseLanguageModel,
) -> SemanticTokenResponse:
    phrase_tokens: SemanticTokenResponse = run_prompt(  # type: ignore
        SemanticToTokensPromptCase(
            phrases=phrase_list,
            tokens=tokens,
            purpose=purpose,
            llm=llm,
        ),
        debug=True,
        session_uuid=session_uuid,
        log_info=log_info,
    )

    return phrase_tokens


def concept_names_from_token_response(
    phrase_tokens: SemanticTokenResponse,
    concepts: dict[str, Concept],
    token_universe: list | None,
) -> list[str]:
    token_universe_internal = token_universe or []
    output: list[str] = []

    for mapping in phrase_tokens:
        token_universe_internal += mapping.tokens
    token_universe_internal = list(set(token_universe_internal))
    for mapping in phrase_tokens.root:
        found = False
        concepts_str_matches = tokens_to_concept(
            mapping.tokens,
            [c for c in concepts.keys()],
            limits=50,
            universe=token_universe_internal,
        )
        logger.debug(f"For phrase {mapping.phrase} got {concepts_str_matches}")
        if concepts_str_matches:
            # logger.info(f"For phrase {mapping.phrase} got {concepts_str_matches}")
            output += concepts_str_matches
            found = True
            continue
        if not found:
            raise ValueError(
                f"Could not find concept for input {mapping.phrase} with tokens {mapping.tokens} and concepts {list(concepts.keys())}"
            )
    return output


def coerce_values(input: List[Union[str, int, float, bool]], dtype=DataType):
    if dtype == DataType.INTEGER:
        return [int(x) for x in input]
    elif dtype == DataType.FLOAT:
        return [float(x) for x in input]
    elif dtype == DataType.BOOL:
        return [bool(x) for x in input]
    return input


def enrich_filter_parent(
    input: FinalFilterResult,
    log_info: bool,
    llm: BaseLanguageModel,
    session_uuid: UUID | None,
):
    try:
        enrich_filter(
            input=input,
            log_info=log_info,
            llm=llm,
            session_uuid=session_uuid,
        )
    except ValueError:
        return


def enrich_filter(
    input: FinalFilterResult,
    log_info: bool,
    llm: BaseLanguageModel,
    session_uuid: UUID | None = None,
):
    if not (input.concept.metadata and input.concept.metadata.description):
        # coerce even without description
        try:
            input.values = coerce_values(input.values, input.concept.datatype)
            return input
        except ValueError as e:
            input.values = coerce_values(
                run_prompt(  # type: ignore
                    FilterRefinementErrorCase(
                        values=input.values,
                        error=str(e),
                        datatype=input.concept.datatype,
                        llm=llm,
                    ),
                    session_uuid=session_uuid,
                    log_info=log_info,
                ).new_values,
                input.concept.datatype,
            )
            return input

    try:
        input.values = coerce_values(
            run_prompt(  # type: ignore
                FilterRefinementCase(
                    values=input.values,
                    description=input.concept.metadata.description,
                    datatype=input.concept.datatype,
                    llm=llm,
                ),
                session_uuid=session_uuid,
                log_info=log_info,
            ).new_values,
            input.concept.datatype,
        )
    except ValueError as e:
        input.values = coerce_values(
            run_prompt(  # type: ignore
                FilterRefinementErrorCase(
                    values=input.values,
                    error=str(e),
                    datatype=input.concept.datatype,
                    llm=llm,
                ),
                session_uuid=session_uuid,
                log_info=log_info,
            ).new_values,
            input.concept.datatype,
        )
        return input


def discover_inputs(
    input_text: str,
    llm: BaseLanguageModel,
    input_environment: Environment,
    debug: bool = False,
    log_info: bool = True,
) -> IntermediateParseResults:
    # the core logic flow

    # DETERMINSTIC: setup logging
    # LLM: semantic extraction
    # LLM: tokenization of all strings (reduce search space over all concepts)
    # DETERMINISTIC: concept candidates from tokens (map reduced search space to candidates)
    # LLM: final selection of concepts and mapping to output roles
    # LLM: enrich filter values
    # DETERMINISTIC: return results

    # DETERMINISTIC: setup logging
    session_uuid = uuid.uuid4()
    env_concepts = input_environment.concepts

    # LLM: semantic extraction
    parsed: InitialParseResponse = run_prompt(  # type:ignore
        SemanticExtractionPromptCase(input_text, llm=llm),
        debug=debug,
        log_info=log_info,
        session_uuid=session_uuid,
    )

    # LLM: tokenization of all strings (reduce search space over all concepts)
    concept_candidates = []
    token_response_mapping: dict[str, SemanticTokenResponse] = {}
    for semantic_category, valid_purposes in {
        "metrics": [Purpose.METRIC],
        "dimensions": [Purpose.KEY, Purpose.PROPERTY, Purpose.CONSTANT],
        "filtering": list(Purpose),
        "order": list(Purpose),
    }.items():
        category_tokens = build_token_list_by_purpose(env_concepts, valid_purposes)
        local_phrases = [
            get_phrase_from_x(x) for x in getattr(parsed, semantic_category)
        ]
        # skip if we have no relevant phrases
        if not local_phrases:
            continue
        if not category_tokens:
            raise ValueError("No tokens for category")
        token_mapping = tokenize_phrases(
            semantic_category,
            local_phrases,
            category_tokens,
            log_info=log_info,
            session_uuid=session_uuid,
            llm=llm,
        )
        token_response_mapping[semantic_category] = token_mapping

    # DETERMINISTIC - generate concept candidates from tokens (map reduced search space to candidates)
    token_universe = set()
    for _, token_mapping_pass_one in token_response_mapping.items():
        for mapping in token_mapping_pass_one:
            for t in mapping.tokens:
                token_universe.add(t)
    token_universe_list = list(token_universe)

    for _, token_mapping_pass_two in token_response_mapping.items():
        for item in token_mapping_pass_two:
            if not all([x in category_tokens] for x in item.tokens):
                invalid = [x for x in item.tokens if x not in category_tokens]
                raise ValueError(
                    f"Phrase {item.phrase} return invalid tokens {invalid}"
                )
        concept_candidates += concept_names_from_token_response(
            token_mapping_pass_two, env_concepts, token_universe=token_universe_list
        )

    # LLM - use our concept candidates to generate the final output
    selections: FinalParseResponse = run_prompt(  # type: ignore
        SelectionPromptCase(
            concept_names=concept_candidates,
            all_concept_names=list(env_concepts.keys()),
            question=input_text,
            llm=llm,
        ),
        debug=debug,
        session_uuid=session_uuid,
        log_info=log_info,
    )
    selected_concepts = list(set(selections.selection))

    final_ordering = [
        FinalOrderResult(concept=env_concepts[order.concept], order=order.order)
        for order in selections.order
    ]

    final_filters_pre = [
        FinalFilterResult(
            concept=env_concepts[filter.concept],
            operator=filter.operator,
            values=filter.values,
        )
        for filter in selections.filtering
    ]

    # LLM: enrich filter values
    for item in final_filters_pre:
        enrich_filter(item, log_info=log_info, session_uuid=session_uuid, llm=llm)

    # DETERMINISTIC: return results
    return IntermediateParseResults(
        select=[env_concepts[c] for c in selected_concepts],
        limit=parsed.limit or 20,
        order=final_ordering,
        filtering=final_filters_pre,
    )


def safe_limit(input: int | None) -> int:
    if not input:
        return DEFAULT_LIMIT
    if input in (-1, 0):
        return DEFAULT_LIMIT
    return input


def parse_order(
    input_concepts: List[Concept], ordering: List[FinalOrderResult] | None
) -> OrderBy:
    default_order = [
        OrderItem(expr=c, order=Ordering.DESCENDING)
        for c in input_concepts
        if c.purpose == Purpose.METRIC
    ]
    if not ordering:
        return OrderBy(items=default_order)
    final = []
    for order in ordering:
        final.append(OrderItem(expr=order.concept, order=order.order))
    return OrderBy(items=final)


def parse_filter(input: FinalFilterResult) -> Comparison | None:
    return Comparison(
        left=input.concept,
        right=input.values[0] if len(input.values) == 1 else input.values,
        operator=input.operator,
    )


def parse_filtering(filtering: List[FinalFilterResult]) -> WhereClause | None:
    base = []
    for item in filtering:
        parsed = parse_filter(item)
        if parsed:
            base.append(parsed)
    if not base:
        return None
    if len(base) == 1:
        return WhereClause(conditional=base[0])
    left: Conditional | Comparison = base.pop()
    while base:
        right = base.pop()
        new = Conditional(left=left, right=right, operator=BooleanOperator.AND)
        left = new
    return WhereClause(conditional=left)


def parse_query(
    input_text: str,
    llm: BaseLanguageModel,
    input_environment: Environment,
    debug: bool = False,
    log_info: bool = True,
):
    intermediate_results = discover_inputs(
        input_text=input_text,
        input_environment=input_environment,
        debug=debug,
        log_info=log_info,
        llm=llm,
    )
    selection = unique(intermediate_results.select, "address")

    order = parse_order(selection, intermediate_results.order)

    filtering = parse_filtering(intermediate_results.filtering)
    # from trilogy.core.models import unique
    # concepts = unique(concepts, 'address')
    if debug:
        print("Concepts found")
        for c in intermediate_results.select:
            print(c.address)
    query = SelectStatement(
        selection=selection,
        limit=safe_limit(intermediate_results.limit),
        order_by=order,
        where_clause=filtering,
    )
    return query


def build_query(
    input_text: str,
    input_environment: Environment,
    llm: BaseLanguageModel,
    debug: bool = False,
    log_info: bool = True,
) -> ProcessedQuery:
    query = parse_query(
        input_text=input_text,
        input_environment=input_environment,
        llm=llm,
        debug=debug,
        log_info=log_info,
    )
    return process_query(statement=query, environment=input_environment)
