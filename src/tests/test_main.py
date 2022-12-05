from tidylib import tidy_document

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    html, error = tidy_document(response.text)
    assert response.status_code == 200
    assert "Berlin" in response.text
    assert "Tokyo" in response.text
    assert "New_York" in response.text
    assert error is ""


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
