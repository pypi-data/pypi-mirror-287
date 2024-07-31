# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.test_case import TestCase

__all__ = [
    "PaginatedApplicationTestCaseOutputWithViews",
    "Item",
    "ItemOutput",
    "ItemOutputGenerationExtraInfo",
    "ItemOutputGenerationExtraInfoChunkExtraInfoSchema",
    "ItemOutputGenerationExtraInfoChunkExtraInfoSchemaChunk",
    "ItemOutputGenerationExtraInfoStringExtraInfoSchema",
    "ItemInteraction",
    "ItemInteractionTraceSpan",
    "ItemMetricScore",
]


class ItemOutputGenerationExtraInfoChunkExtraInfoSchemaChunk(BaseModel):
    metadata: object

    text: str


class ItemOutputGenerationExtraInfoChunkExtraInfoSchema(BaseModel):
    chunks: List[ItemOutputGenerationExtraInfoChunkExtraInfoSchemaChunk]

    schema_type: Optional[Literal["CHUNKS"]] = None


class ItemOutputGenerationExtraInfoStringExtraInfoSchema(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


ItemOutputGenerationExtraInfo = Annotated[
    Union[ItemOutputGenerationExtraInfoChunkExtraInfoSchema, ItemOutputGenerationExtraInfoStringExtraInfoSchema],
    PropertyInfo(discriminator="schema_type"),
]


class ItemOutput(BaseModel):
    generation_output: str

    generation_extra_info: Optional[ItemOutputGenerationExtraInfo] = None


class ItemInteractionTraceSpan(BaseModel):
    id: str
    """Identifies the application step"""

    application_interaction_id: str
    """The id of the application insight this step belongs to"""

    duration_ms: int
    """How much time the step took in milliseconds(ms)"""

    node_id: str
    """The id of the node in the application_variant config that emitted this insight"""

    operation_status: Literal["SUCCESS", "ERROR"]
    """An enumeration."""

    operation_type: str
    """Type of the operation, e.g. RERANKING"""

    start_timestamp: datetime
    """The start time of the step"""

    operation_input: Optional[object] = None
    """The JSON representation of the input that this step received"""

    operation_metadata: Optional[object] = None
    """The JSON representation of the metadata insights emitted through the execution.

    This can differ based on different types of operations
    """

    operation_output: Optional[object] = None
    """The JSON representation of the output that this step emitted"""


class ItemInteraction(BaseModel):
    id: str

    application_spec_id: str

    application_variant_id: str

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    duration_ms: int
    """How much time the step took in milliseconds(ms)"""

    input: object

    operation_status: Literal["SUCCESS", "ERROR"]
    """An enumeration."""

    output: object

    start_timestamp: datetime

    chat_thread_id: Optional[str] = None

    trace_spans: Optional[List[ItemInteractionTraceSpan]] = None


class ItemMetricScore(BaseModel):
    category: Literal["accuracy", "quality", "retrieval", "trust-and-safety"]
    """An enumeration."""

    metric_type: Literal[
        "answer-correctness",
        "answer-relevance",
        "faithfulness",
        "context-recall",
        "coherence",
        "grammar",
        "moderation",
        "safety",
        "safety-bias-and-stereotyping",
        "safety-opinions-disputed-topics",
        "safety-unethical-harmful-activities",
        "safety-copyright-violations",
        "safety-harmful-content",
        "safety-privacy-violations",
    ]

    score: Optional[float] = None


class Item(BaseModel):
    id: str
    """The unique identifier of the entity."""

    account_id: str
    """The ID of the account that owns the given entity."""

    application_variant_id: str

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    evaluation_dataset_id: str

    output: ItemOutput

    schema_type: Literal["GENERATION"]
    """An enumeration."""

    test_case_id: str

    application_interaction_id: Optional[str] = None

    interaction: Optional[ItemInteraction] = None

    metric_scores: Optional[List[ItemMetricScore]] = None

    test_case_version: Optional[TestCase] = None


class PaginatedApplicationTestCaseOutputWithViews(BaseModel):
    current_page: int
    """The current page number."""

    items: List[Item]
    """The data returned for the current page."""

    items_per_page: int
    """The number of items per page."""

    total_item_count: int
    """The total number of items of the query"""
