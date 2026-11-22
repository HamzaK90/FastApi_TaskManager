from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.tag import Tag


class TagStorage:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_or_build(self, names: list[str]) -> list[Tag]:
        unique_names = list(dict.fromkeys(names))
        existing = {
            tag.name: tag
            for tag in self._session.scalars(select(Tag).where(Tag.name.in_(unique_names)))
        }
        return [existing.get(name) or Tag(name=name) for name in unique_names]
