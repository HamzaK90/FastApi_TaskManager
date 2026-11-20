from collections.abc import Iterator

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings
from app.database import get_db
from app.main import app

test_engine = create_engine(settings.test_database_url)
TestSessionLocal = sessionmaker(bind=test_engine, autoflush=False, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
def migrated_database() -> Iterator[None]:
    alembic_config = Config("alembic.ini")
    alembic_config.attributes["database_url"] = settings.test_database_url
    command.upgrade(alembic_config, "head")
    yield
    command.downgrade(alembic_config, "base")


@pytest.fixture
def client() -> Iterator[TestClient]:
    def get_test_db() -> Iterator[Session]:
        with TestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

    with test_engine.begin() as connection:
        connection.execute(text("delete from tasks"))
