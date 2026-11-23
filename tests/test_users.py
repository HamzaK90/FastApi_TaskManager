from fastapi.testclient import TestClient


def test_create_user(client: TestClient) -> None:
    response = client.post("/users", json={"name": "Omar Khalil", "email": "omar@example.com"})

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Omar Khalil"
    assert body["email"] == "omar@example.com"
    assert isinstance(body["id"], int)


def test_create_user_with_duplicate_email_returns_409(client: TestClient, user_id: int) -> None:
    response = client.post("/users", json={"name": "Someone Else", "email": "sara@example.com"})

    assert response.status_code == 409


def test_create_user_with_invalid_email_returns_422(client: TestClient) -> None:
    response = client.post("/users", json={"name": "Omar Khalil", "email": "not-an-email"})

    assert response.status_code == 422


def test_get_user(client: TestClient, user_id: int) -> None:
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["email"] == "sara@example.com"


def test_get_missing_user_returns_404(client: TestClient) -> None:
    response = client.get("/users/999999")

    assert response.status_code == 404


def test_list_user_tasks_returns_only_that_users_tasks(client: TestClient, user_id: int) -> None:
    other_id = client.post("/users", json={"name": "Omar Khalil", "email": "omar@example.com"}).json()["id"]
    client.post("/tasks", json={"title": "Sara 1", "user_id": user_id})
    client.post("/tasks", json={"title": "Omar 1", "user_id": other_id})
    client.post("/tasks", json={"title": "Sara 2", "user_id": user_id})

    response = client.get(f"/users/{user_id}/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["Sara 1", "Sara 2"]


def test_list_tasks_of_user_without_tasks_is_empty(client: TestClient, user_id: int) -> None:
    response = client.get(f"/users/{user_id}/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_of_missing_user_returns_404(client: TestClient) -> None:
    response = client.get("/users/999999/tasks")

    assert response.status_code == 404
