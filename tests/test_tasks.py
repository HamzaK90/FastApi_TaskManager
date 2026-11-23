from fastapi.testclient import TestClient


def create_task(client: TestClient, user_id: int, **fields: object) -> dict:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": user_id, **fields})
    assert response.status_code == 201
    return response.json()


def test_create_task(client: TestClient, user_id: int) -> None:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": user_id})

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Buy milk"
    assert body["description"] == ""
    assert body["completed"] is False
    assert body["user_id"] == user_id
    assert isinstance(body["id"], int)


def test_create_task_strips_whitespace(client: TestClient, user_id: int) -> None:
    body = create_task(client, user_id, title="  Buy milk  ")

    assert body["title"] == "Buy milk"


def test_create_task_with_empty_title_returns_422(client: TestClient, user_id: int) -> None:
    response = client.post("/tasks", json={"title": "", "user_id": user_id})

    assert response.status_code == 422


def test_create_task_with_unknown_field_returns_422(client: TestClient, user_id: int) -> None:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": user_id, "priority": "high"})

    assert response.status_code == 422


def test_create_task_without_user_returns_422(client: TestClient) -> None:
    response = client.post("/tasks", json={"title": "Buy milk"})

    assert response.status_code == 422


def test_create_task_for_missing_user_returns_404(client: TestClient) -> None:
    response = client.post("/tasks", json={"title": "Buy milk", "user_id": 999999})

    assert response.status_code == 404


def test_list_tasks_is_empty_at_start(client: TestClient) -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_in_creation_order(client: TestClient, user_id: int) -> None:
    create_task(client, user_id, title="First")
    create_task(client, user_id, title="Second")

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["First", "Second"]


def test_get_task(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id, title="Report", description="Q3 numbers")

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_get_missing_task_returns_404(client: TestClient) -> None:
    response = client.get("/tasks/999999")

    assert response.status_code == 404


def test_patch_only_changes_sent_fields(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id, title="Report", description="Q3")

    response = client.patch(f"/tasks/{created['id']}", json={"completed": True})

    assert response.status_code == 200
    body = response.json()
    assert body["completed"] is True
    assert body["title"] == "Report"
    assert body["description"] == "Q3"


def test_patch_is_saved_in_database(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id)

    client.patch(f"/tasks/{created['id']}", json={"title": "Buy bread"})
    response = client.get(f"/tasks/{created['id']}")

    assert response.json()["title"] == "Buy bread"


def test_patch_missing_task_returns_404(client: TestClient) -> None:
    response = client.patch("/tasks/999999", json={"completed": True})

    assert response.status_code == 404


def test_delete_task(client: TestClient, user_id: int) -> None:
    created = create_task(client, user_id)

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404


def test_delete_missing_task_returns_404(client: TestClient) -> None:
    response = client.delete("/tasks/999999")

    assert response.status_code == 404
