from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


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
