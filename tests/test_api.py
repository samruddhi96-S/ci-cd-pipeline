import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}


def test_add_api(client):
    response = client.get("/calc/add?a=2&b=3")
    assert response.get_json()["result"] == 5


def test_divide_by_zero_api(client):
    response = client.get("/calc/divide?a=1&b=0")
    assert response.status_code == 400


def test_bad_input(client):
    response = client.get("/calc/add?a=abc&b=3")
    assert response.status_code == 400


def test_unknown_operation(client):
    response = client.get("/calc/power?a=2&b=3")
    assert response.status_code == 404
