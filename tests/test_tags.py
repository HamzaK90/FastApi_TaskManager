from fastapi.testclient import TestClient


def create_task(client: TestClient, user_id: int, **fields: object) -> dict:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": user_id, **fields})
    assert response.status_code == 201
    return response.json()


def tag_names(task: dict) -> list[str]:
    return [tag["name"] for tag in task["tags"]]


def test_create_task_without_tags_has_empty_list(client: TestClient, user_id: int) -> None:
    body = create_task(client, user_id)

    assert body["tags"] == []


def test_create_task_with_tags(client: TestClient, user_id: int) -> None:
    body = create_task(client, user_id, tags=["work", "urgent"])

    assert tag_names(body) == ["work", "urgent"]


def test_tag_names_are_lowercased_and_deduplicated(client: TestClient, user_id: int) -> None:
    body = create_task(client, user_id, tags=["Work", " work ", "WORK"])

    assert tag_names(body) == ["work"]


def test_existing_tag_is_reused(client: TestClient, user_id: int) -> None:
    first = create_task(client, user_id, title="First", tags=["work"])
    second = create_task(client, user_id, title="Second", tags=["work"])

    assert first["tags"][0]["id"] == second["tags"][0]["id"]


def test_add_tags_to_task(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id, tags=["work"])

    response = client.post(f"/tasks/{created['id']}/tags", json={"tags": ["home"]})

    assert response.status_code == 200
    assert tag_names(response.json()) == ["work", "home"]


def test_adding_existing_tag_does_not_duplicate_it(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id, tags=["work"])

    response = client.post(f"/tasks/{created['id']}/tags", json={"tags": ["Work", "home"]})

    assert response.status_code == 200
    assert tag_names(response.json()) == ["work", "home"]


def test_added_tags_are_saved(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id)

    client.post(f"/tasks/{created['id']}/tags", json={"tags": ["home"]})
    response = client.get(f"/tasks/{created['id']}")

    assert tag_names(response.json()) == ["home"]


def test_add_tags_to_missing_task_returns_404(client: TestClient) -> None:
    response = client.post("/tasks/999999/tags", json={"tags": ["work"]})

    assert response.status_code == 404


def test_add_empty_tag_list_returns_422(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id)

    response = client.post(f"/tasks/{created['id']}/tags", json={"tags": []})

    assert response.status_code == 422


def test_tag_name_too_long_returns_422(client: TestClient, user_id: int) -> None:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": user_id, "tags": ["x" * 51]})

    assert response.status_code == 422
