from typing import Literal, Self

from sqlalchemy import Select, or_, select
from sqlalchemy.orm import selectinload

from app.models.tag import Tag
from app.models.task import Task


class TaskQueryBuilder:
    def __init__(self) -> None:
        self._query: Select[tuple[Task]] = select(Task)

    def with_status(self, status: Literal["pending", "completed"] | None) -> Self:
        if status is not None:
            self._query = self._query.where(Task.completed == (status == "completed"))
        return self

    def with_tag(self, tag: str | None) -> Self:
        if tag is not None:
            self._query = self._query.where(Task.tags.any(Tag.name == tag))
        return self

    def with_search(self, search: str | None) -> Self:
        if search is not None:
            self._query = self._query.where(
                or_(
                    Task.title.icontains(search, autoescape=True),
                    Task.description.icontains(search, autoescape=True),
                )
            )
        return self

    def build(self) -> Select[tuple[Task]]:
        return self._query.options(selectinload(Task.tags)).order_by(Task.id)
