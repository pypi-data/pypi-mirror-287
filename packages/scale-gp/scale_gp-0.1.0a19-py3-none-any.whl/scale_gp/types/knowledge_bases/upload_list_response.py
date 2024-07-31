# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "UploadListResponse",
    "DataSourceConfig",
    "DataSourceConfigS3DataSourceConfig",
    "DataSourceConfigSharePointDataSourceConfig",
    "DataSourceConfigGoogleDriveDataSourceConfig",
    "DataSourceConfigAzureBlobStorageDataSourceConfig",
    "DataSourceConfigLocalChunksSourceConfig",
    "DataSourceConfigLocalFileSourceConfig",
    "DataSourceConfigConfluenceDataSourceConfig",
    "DataSourceConfigSlackDataSourceConfig",
    "ChunkingStrategyConfig",
    "ChunkingStrategyConfigCharacterChunkingStrategyConfig",
    "ChunkingStrategyConfigTokenChunkingStrategyConfig",
    "ChunkingStrategyConfigCustomChunkingStrategyConfig",
]


class DataSourceConfigS3DataSourceConfig(BaseModel):
    aws_account_id: str
    """AWS account ID that owns the S3 bucket."""

    aws_region: str
    """AWS region where the S3 bucket is located."""

    s3_bucket: str
    """Name of the S3 bucket where the data is stored."""

    source: Literal["S3"]

    s3_prefix: Optional[str] = None
    """Prefix of the S3 bucket where the data is stored.

    If not specified, the entire bucket will be used.
    """


class DataSourceConfigSharePointDataSourceConfig(BaseModel):
    client_id: str
    """Client ID associated with this SharePoint site"""

    site_id: str
    """
    Site ID for this SharePoint site, can be found at
    https://[hostname].sharepoint.com/sites/[site name]/\\__api/site/id
    """

    source: Literal["SharePoint"]

    tenant_id: str
    """Tenant ID that the SharePoint site is within"""

    folder_path: Optional[str] = None
    """Nested folder path to read files from the root of the site.

    Please omit the leading slash. Example: 'Documents/sub_directory'
    """

    recursive: Optional[bool] = None
    """Recurse through the folder contents, default is True."""


class DataSourceConfigGoogleDriveDataSourceConfig(BaseModel):
    drive_id: str
    """ID associated with the Google Drive to retrieve contents from"""

    source: Literal["GoogleDrive"]


class DataSourceConfigAzureBlobStorageDataSourceConfig(BaseModel):
    container_url: str
    """
    The full URL of the container such as
    'https://your-account-name.blob.core.windows.net/your-container-name'
    """

    source: Literal["AzureBlobStorage"]


class DataSourceConfigLocalChunksSourceConfig(BaseModel):
    artifact_name: str
    """The file name assigned to the artifact, containing a file extension.

    Adding an extension is mandatory, to allow detecting file types for text
    extraction.
    """

    artifact_uri: str
    """
    A unique identifier for an artifact within the knowledge base, such as full path
    in a directory or file system.
    """

    source: Literal["LocalChunks"]

    deduplication_strategy: Optional[Literal["Overwrite", "Fail"]] = None
    """An enumeration."""


class DataSourceConfigLocalFileSourceConfig(BaseModel):
    source: Literal["LocalFile"]

    deduplication_strategy: Optional[Literal["Overwrite", "Fail"]] = None
    """An enumeration."""


class DataSourceConfigConfluenceDataSourceConfig(BaseModel):
    source: Literal["Confluence"]

    space_key: str
    """Confluence space key to retrieve contents from.

    See https://support.atlassian.com/confluence-cloud/docs/choose-a-space-key
    """


class DataSourceConfigSlackDataSourceConfig(BaseModel):
    channel_id: str
    """Slack Channel or Conversation ID to retrieve history from.

    Open channel details and find the ID at bottom of 'About' section.
    """

    source: Literal["Slack"]


DataSourceConfig = Annotated[
    Union[
        DataSourceConfigS3DataSourceConfig,
        DataSourceConfigSharePointDataSourceConfig,
        DataSourceConfigGoogleDriveDataSourceConfig,
        DataSourceConfigAzureBlobStorageDataSourceConfig,
        DataSourceConfigLocalChunksSourceConfig,
        DataSourceConfigLocalFileSourceConfig,
        DataSourceConfigConfluenceDataSourceConfig,
        DataSourceConfigSlackDataSourceConfig,
    ],
    PropertyInfo(discriminator="source"),
]


class ChunkingStrategyConfigCharacterChunkingStrategyConfig(BaseModel):
    strategy: Literal["character"]

    chunk_overlap: Optional[int] = None
    """Number of characters to overlap between chunks.

    If not specified, an overlap of 200 will be used. For example if the chunk size
    is 3 and the overlap size is 1, and the text to chunk is 'abcde', the chunks
    will be 'abc', 'cde'.
    """

    chunk_size: Optional[int] = None
    """Maximum number of characters in each chunk.

    If not specified, a chunk size of 1000 will be used.
    """

    separator: Optional[str] = None
    """Character designating breaks in input data.

    Text data will first be split into sections by this separator, then each section
    will be split into chunks of size `chunk_size`.
    """


class ChunkingStrategyConfigTokenChunkingStrategyConfig(BaseModel):
    strategy: Literal["token"]

    chunk_overlap: Optional[int] = None
    """Number of tokens to overlap between chunks.

    If not specified, an overlap of 0 will be used. Not this if only followed
    approximately.
    """

    max_chunk_size: Optional[int] = None
    """Maximum number of tokens in each chunk.

    If not specified, a maximum chunk size of 600 will be used.
    """

    separator: Optional[str] = None
    """Character designating breaks in input data.

    Text data will first be split into sections by this separator, then each section
    will be split into chunks of size `chunk_size`.
    """

    target_chunk_size: Optional[int] = None
    """Target number of tokens in each chunk.

    If not specified, a target chunk size of 200 will be used.
    """


class ChunkingStrategyConfigCustomChunkingStrategyConfig(BaseModel):
    endpoint: str
    """Endpoint path to call for custom chunking"""

    strategy: Literal["custom"]

    params: Optional[object] = None
    """Parameters that will be appended to the body of the request for the chunk."""


ChunkingStrategyConfig = Annotated[
    Union[
        ChunkingStrategyConfigCharacterChunkingStrategyConfig,
        ChunkingStrategyConfigTokenChunkingStrategyConfig,
        ChunkingStrategyConfigCustomChunkingStrategyConfig,
    ],
    PropertyInfo(discriminator="strategy"),
]


class UploadListResponse(BaseModel):
    id: str

    data_source_config: DataSourceConfig

    knowledge_base_id: str

    chunking_strategy_config: Optional[ChunkingStrategyConfig] = None

    created_at: Union[str, datetime, None] = None

    created_by_schedule_id: Optional[str] = None

    data_source_idempotency_key: Optional[str] = None

    status: Optional[str] = None

    status_reason: Optional[str] = None

    updated_at: Union[str, datetime, None] = None
