from fastapi.testclient import TestClient

from server import __version__
from server.main import app

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


EXPECTED_RESPONSE_USERS_FOLLOWERS: list = [
    {"name": "Andras Nagy", "email": "andras@nagy.dk"},
    {"name": "Sara Horvath", "email": "sara@horvath.dk"},
]


def test_user_followers_correct_with_followers():
    response = client.get("/user/followers/1")
    assert response.status_code in [200]
    assert response.json() == EXPECTED_RESPONSE_USERS_FOLLOWERS


def test_user_followers_correct_without_followers():
    response = client.get("/user/followers/4")
    assert response.status_code in [200]
    assert response.json() == []


def test_user_followers_incorrect_no_person_id():
    response = client.get("/user/followers/5")
    assert response.status_code in [404]
