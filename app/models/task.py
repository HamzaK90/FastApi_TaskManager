from datetime import datetime

from sqlalchemy import String, false, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500), default="", server_default="")
    completed: Mapped[bool] = mapped_column(default=False, server_default=false())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
