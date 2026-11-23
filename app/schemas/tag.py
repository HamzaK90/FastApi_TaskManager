from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

TagName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_lower=True, min_length=1, max_length=50),
]


class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class TagsAdd(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tags: list[TagName] = Field(min_length=1)
