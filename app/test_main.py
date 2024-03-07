from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200


def test_read_user():
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "user1"}


def test_create_user():
    response = client.post("/api/users", json={"name": "user2"})
    assert response.status_code == 201
    assert response.json() == {
        "email": "admin@example.com",
        "remember_token": None,
        "updated_at": "2024-01-26T17:28:42",
        "name": "Admin User",
        "id": "1",
        "nim": "A12345",
        "score": 150,
        "email_verified_at": None,
        "created_at": "2024-01-26T17:28:42",
    }

