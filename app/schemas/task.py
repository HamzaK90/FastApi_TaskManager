from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from app.schemas.tag import TagName, TagResponse


class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    user_id: int = Field(gt=0)
    tags: list[TagName] = Field(default_factory=list)

class TaskUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    title: str = Field(default=None, min_length=1, max_length=100)
    description: str = Field(default=None, max_length=500)
    completed: bool = Field(default=None) 


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    completed: bool 
    user_id: int
    tags: list[TagResponse]

class TaskFilters(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    status: Literal["pending", "completed"] | None = None
    tag: TagName | None = None
    search: str | None = Field(default=None, min_length=1, max_length=100)
