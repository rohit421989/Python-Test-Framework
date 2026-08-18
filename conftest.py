import pytest


from config.config import Config
from framework.api.api_client import APIClient
from framework.database.db_client import DBClient


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


@pytest.fixture
def db_client():

    client = DBClient(
        "sqlite:///test.db"
    )

    yield client

    client.close()


@pytest.fixture
def clean_users_table(db_client):

    db_client.execute_update(
        """
        DROP TABLE IF EXISTS users
        """
    )

    yield

    db_client.execute_update(
        """
        DROP TABLE IF EXISTS users
        """
    )    

