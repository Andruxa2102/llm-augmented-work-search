from pydantic import BaseModel, Field, field_validator, HttpUrl, ValidationInfo, ConfigDict
from typing import Dict


class RateLimitConfig(BaseModel):
    """Controls how many requests can be made to the endpoint to prevent abuse and manage infrastructure costs"""
    model_config = ConfigDict(extra='forbid')
    min_delay_s: float = Field(ge=0.5, description="Min delay")
    max_delay_s: float = Field(ge=0.5, description="Max delay")
    max_requests: int = 5
    period_seconds: int = 2

    @field_validator('max_delay_s')
    @classmethod
    def compare_delays(cls, value, info: ValidationInfo):
        if 'min_delay_s' in info.data and value < info.data['min_delay_s']:
            raise ValueError('max_delay_s must be >= min_delay_s')
        return value


class SourceConfig(BaseModel):
    """Configuration for collection source"""
    model_config = ConfigDict(extra='forbid')

    base_url: HttpUrl
    rate_limit: RateLimitConfig
    pagination_param: str = "page"
    enabled: bool = True
    query: str = ""
    headers_file: str | None = None
    parser_type: str = "html_bs4"


class SourcesConfig(BaseModel):
    """Aggregated Sources Configuration"""
    model_config = ConfigDict(extra='forbid')
    sources: Dict[str, SourceConfig]

