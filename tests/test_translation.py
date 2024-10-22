from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_translation():
    with TestClient(app) as client:
        response = client.post("/v1/translate/", json={"text": "Қазақстан Республикасының астанасы қай қала?"})
        assert response.status_code == 200
        assert "translated_text" in response.json()

def test_healthcheck():
    with TestClient(app) as client:
        response = client.get("/v1/healthcheck/")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
