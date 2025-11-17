from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class AtheonUnitFetchAndIntegrateModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: Annotated[str, Field(min_length=2)]
    base_content: Annotated[str, Field(min_length=10)]
    include_ad_units: Annotated[bool, Field(default=False)]
    use_user_intent_as_filter: Annotated[bool | None, Field(default=None)]
