from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        assert client.get("/health").status_code == 200

def test_subscription():
    with TestClient(app) as client:
        response = client.post("/api/subscribe", json={"email": "learner@example.com"})
        assert response.status_code == 201
