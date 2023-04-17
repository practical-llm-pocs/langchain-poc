import pytest
from fastapi.testclient import TestClient
from src.api.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_get_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_get_hello_with_name(client):
    response = client.get("/hello/Doge")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Doge!"}
