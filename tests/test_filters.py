import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def tasks(client: TestClient, user_id: int) -> None:
    def create(title: str, description: str = "", tags: list[str] | None = None, completed: bool = False) -> None:
        body = {"title": title, "description": description, "user_id": user_id, "tags": tags or []}
        task = client.post("/tasks", json=body).json()
        if completed:
            client.patch(f"/tasks/{task['id']}", json={"completed": True})

    create("Write report", "Q3 numbers", tags=["work"])
    create("Buy milk", tags=["home"])
    create("Send invoice", "monthly REPORT for client", tags=["work", "urgent"], completed=True)
    create("Clean desk")


def titles(client: TestClient, query: str) -> list[str]:
    response = client.get(f"/tasks{query}")
    assert response.status_code == 200
    return [task["title"] for task in response.json()]


def test_no_filters_returns_all_tasks(client: TestClient, tasks: None) -> None:
    assert titles(client, "") == ["Write report", "Buy milk", "Send invoice", "Clean desk"]


def test_filter_pending(client: TestClient, tasks: None) -> None:
    assert titles(client, "?status=pending") == ["Write report", "Buy milk", "Clean desk"]


def test_filter_completed(client: TestClient, tasks: None) -> None:
    assert titles(client, "?status=completed") == ["Send invoice"]


def test_filter_by_tag(client: TestClient, tasks: None) -> None:
    assert titles(client, "?tag=work") == ["Write report", "Send invoice"]


def test_filter_by_tag_is_case_insensitive(client: TestClient, tasks: None) -> None:
    assert titles(client, "?tag=WORK") == ["Write report", "Send invoice"]


def test_filter_by_unknown_tag_returns_empty(client: TestClient, tasks: None) -> None:
    assert titles(client, "?tag=garden") == []


def test_search_matches_title_and_description_ignoring_case(client: TestClient, tasks: None) -> None:
    assert titles(client, "?search=report") == ["Write report", "Send invoice"]


def test_search_percent_sign_is_not_a_wildcard(client: TestClient, tasks: None) -> None:
    assert titles(client, "?search=%25") == []


def test_filters_combine_with_and(client: TestClient, tasks: None) -> None:
    assert titles(client, "?status=pending&tag=work&search=report") == ["Write report"]


def test_invalid_status_returns_422(client: TestClient) -> None:
    response = client.get("/tasks?status=done")

    assert response.status_code == 422


def test_unknown_filter_returns_422(client: TestClient) -> None:
    response = client.get("/tasks?stauts=pending")

    assert response.status_code == 422
