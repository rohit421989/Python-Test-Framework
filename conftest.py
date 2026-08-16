import pytest


from config.config import Config
from framework.api.api_client import APIClient


@pytest.fixture
def login_credentials():
    return {
        "username": "admin",
        "password": "admin123"
    }


@pytest.fixture
def test_user():
    print("\n Creating test user")

    user={
        "username": "testuser",
        "email": "test@example.com"
    }

    yield user
    print("\n Deleting test user")
    #yield is just like return with added feature when the subsequent lines after yield get executed after the calling function has run


@pytest.fixture
def api_client():

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Config.API_TOKEN}"
    }

    return APIClient(
        base_url=Config.get_base_url(),
        headers=headers
    )  