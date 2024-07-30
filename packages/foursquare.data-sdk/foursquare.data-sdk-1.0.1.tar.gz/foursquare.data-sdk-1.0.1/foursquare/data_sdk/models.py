# Pydantic validators are class methods, so require the first param to be `cls`, but
# pylint can't recognize this: https://github.com/samuelcolvin/pydantic/issues/568
# pylint: disable=no-self-argument
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
    model_validator,
)
from typing_extensions import Annotated

from foursquare.data_sdk.enums import (
    AggregationMethod,
    DataConnectorType,
    DatasetType,
    Dtype,
    HexTileFieldType,
    JobSize,
    MediaType,
    PermissionType,
    ResourceType,
    TileMode,
    TimeInterval,
)
from foursquare.data_sdk.types import AccessToken, RefreshToken


class Credentials(BaseModel):
    access_token: AccessToken
    refresh_token: RefreshToken
    scope: str
    expires_in: int
    token_type: str


class DatasetMetadata(BaseModel):
    """A model representing metadata for a Foursquare Studio Dataset"""

    media_type: Optional[Union[MediaType, StrictStr]] = Field(None, alias="contentType")
    size: Optional[StrictInt] = None
    source: Optional[StrictStr] = None
    tileset_data_url: Optional[StrictStr] = Field(None, alias="tilesetDataUrl")
    tileset_metadata_url: Optional[StrictStr] = Field(None, alias="tilesetMetadataUrl")
    image_url: Optional[StrictStr] = Field(None, alias="imageUrl")
    metadata_url: Optional[StrictStr] = Field(None, alias="metadataUrl")
    data_status: Optional[StrictStr] = Field(None, alias="dataStatus")
    model_config = ConfigDict(populate_by_name=True)


class DatasetUpdateParams(BaseModel):
    """A model representing creation and update parameters for Datasets"""

    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    model_config = ConfigDict(populate_by_name=True)


class DataConnector(BaseModel):
    """A model representing a data connector"""

    id: UUID
    name: StrictStr
    description: Optional[StrictStr] = None
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    type: DataConnectorType
    model_config = ConfigDict(populate_by_name=True)


class Dataset(BaseModel):
    """A model representing a Foursquare Studio Dataset"""

    id: UUID
    name: StrictStr
    type: DatasetType
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    description: Optional[StrictStr] = None
    is_valid: StrictBool = Field(..., alias="isValid")
    data_connector: Optional[DataConnector] = Field(None, alias="dataConnection")
    metadata: DatasetMetadata
    model_config = ConfigDict(populate_by_name=True)


class MapState(BaseModel):
    """A model representing a Foursquare Studio Map Starte"""

    id: UUID
    # data contains the actual map configuration, and should be modeled more concretely than a
    # generic Dictionary.
    # TODO: revisit this once we have a style building strategy
    data: Dict
    model_config = ConfigDict(populate_by_name=True)


class MapUpdateParams(BaseModel):
    """A model respresenting creation and update parameters for Foursquare Studio Maps"""

    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    latest_state: Optional[MapState] = Field(None, alias="latestState")
    datasets: Optional[List[UUID]] = None
    model_config = ConfigDict(populate_by_name=True)


class Map(BaseModel):
    """A model representing a Foursquare Studio Map"""

    id: UUID
    name: StrictStr
    description: Optional[StrictStr] = None
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    latest_state: Optional[MapState] = Field(None, alias="latestState")
    datasets: Optional[List[Dataset]] = None
    model_config = ConfigDict(populate_by_name=True)


class ConnectorQuery(BaseModel):
    """A model representing a SQL query to execute or create a dataset from"""

    connector_id: UUID = Field(..., alias="connectionId")
    query: StrictStr
    model_config = ConfigDict(populate_by_name=True)


class HexTileMetadataField(BaseModel):
    """A model representing a field (column) within hextile dataset metadata"""

    name: StrictStr
    type: HexTileFieldType
    domain: Optional[Tuple[float, float]] = None
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class HexTileMetadata(BaseModel):
    """A model representing an metadata for a hextile dataset"""

    fields: List[HexTileMetadataField]
    name: Optional[StrictStr] = None
    min_zoom: StrictInt = Field(..., alias="minZoom")
    max_zoom: StrictInt = Field(..., alias="maxZoom")
    resolution_offset: StrictInt = Field(..., alias="resolutionOffset")
    version: StrictStr
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class HexTileOutputColumnConfig(BaseModel):
    source_column: StrictStr = Field(..., alias="sourceColumn")
    """Column name in source dataset"""

    target_column: StrictStr = Field(..., alias="targetColumn")
    """Column name in target dataset"""

    agg_method: Optional[AggregationMethod] = Field(..., alias="aggMethod")
    """Aggregation method to use for column"""

    dtype: Optional[Dtype] = None
    """Dtype to use for column"""
    model_config = ConfigDict(populate_by_name=True)


H3Resolution = Annotated[StrictInt, Field(ge=0, le=15)]


class TilingBaseModel(BaseModel):
    """Config for tiling process"""

    source: UUID
    """Source Dataset"""

    @field_validator("source", mode="before")
    @classmethod
    def _coerce_source_to_uuid(cls, v: Any) -> Any:
        if isinstance(v, Dataset):
            return v.id

        return v

    target: Optional[UUID] = None
    """Target Dataset"""

    @field_validator("target", mode="before")
    @classmethod
    def _coerce_target_to_uuid(cls, v: Any) -> Any:
        if isinstance(v, Dataset):
            return v.id

        return v


class HexTileConfig(TilingBaseModel):
    """Config for hextiling process"""

    @model_validator(mode="after")  # type: ignore[arg-type]
    @classmethod
    def _validate_source_columns(cls, config: "HexTileConfig") -> "HexTileConfig":
        source_hex_column = config.source_hex_column
        source_lat_column = config.source_lat_column
        source_lng_column = config.source_lng_column
        source_time_column = config.source_time_column
        time_intervals = config.time_intervals

        if source_hex_column:
            if source_lat_column or source_lng_column:
                raise ValueError(
                    "Only provide source_hex_column or source_lat_column and source_lng_column, but not all three"
                )
        else:
            if not source_lat_column or not source_lng_column:
                raise ValueError(
                    "Must provide either source_hex_column or source_lat_column and source_lng_column"
                )

        if time_intervals and not source_time_column:
            raise ValueError(
                "Must provide source_time_column when passing in time_interval"
            )

        return config

    source_hex_column: Optional[StrictStr] = Field(None, alias="sourceHexColumn")
    """Name of the hex column in the source dataset"""

    source_lat_column: Optional[StrictStr] = Field(None, alias="sourceLatColumn")
    """Name of the lat column in the source dataset"""

    source_lng_column: Optional[StrictStr] = Field(None, alias="sourceLngColumn")
    """Name of the lng column in the source dataset"""

    source_time_column: Optional[StrictStr] = Field(None, alias="sourceTimeColumn")
    """Name of the time column, in the source dataset"""

    time_intervals: Optional[List[TimeInterval]] = Field(
        None, alias="timeIntervals", min_length=1
    )
    """List of time intervals to use for temporal datasets"""

    target_res_offset: Optional[H3Resolution] = Field(None, alias="targetResOffset")
    """
    Offset between the resolution of the tile to the resolution of the data within it
    """

    finest_resolution: Optional[H3Resolution] = Field(None, alias="finestResolution")
    """
    Finest resolution for the data hexes within a tile (when creating a tileset from lat/lng columns)
    """

    experimental_tile_mode: Optional[TileMode] = Field(None, alias="tileMode")

    output_columns: Optional[List[HexTileOutputColumnConfig]] = Field(
        None, alias="outputColumns", min_length=1
    )

    experimental_positional_indexes: Optional[StrictBool] = Field(
        None, alias="positionalIndexes"
    )

    job_size: Optional[JobSize] = Field(None, alias="jobSize")
    model_config = ConfigDict(populate_by_name=True)


class VectorTileConfig(TilingBaseModel):

    source_lat_column: Optional[StrictStr] = Field(None, alias="sourceLatColumn")
    """Name of the lat column in the source dataset"""

    source_lng_column: Optional[StrictStr] = Field(None, alias="sourceLngColumn")
    """Name of the lng column in the source dataset"""

    attributes: Optional[List[StrictStr]] = None
    """List of attributes to keep in vector tiling. Leave blank to keep all."""

    exclude_all_attributes: Optional[bool] = Field(None, alias="excludeAllAttributes")
    """Whether to exclude all attributes in vector tiling."""

    tile_size_kb: Optional[int] = Field(None, alias="tileSizeKb")
    """Maximum tile size (in kilobytes) for each generated tile."""


class UserPermission(BaseModel):
    email: StrictStr
    permission: PermissionType


class CategorizedPermissions(BaseModel):
    organization: Optional[PermissionType] = None
    users: Optional[List[UserPermission]] = None


class PermissionsConfig(BaseModel):
    resource_type: Union[ResourceType, str] = Field(..., alias="resourceType")
    resource_id: Union[str, UUID] = Field(..., alias="resourceId")
    permissions: Union[CategorizedPermissions, Dict]
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
