import pytest


from framework.api.api_client import APIClient
from test_data.login_data import VALID_USERNAME,VALID_PASSWORD

@pytest.mark.smoke
@pytest.mark.parametrize(
    "username, password, expected",
    [
      ("admin", "admin123", True),
        ("admin", "wrong123", False),
        ("wronguser", "admin123", False),
        ("", "admin123", False),
        ("admin", "", False),
])
#Note Key rule: @pytest.mark.parametrize only applies to the function directly below it
#A decorator attaches to one function only — the one immediately following it. It does not cascade down to other functions later in the file.


def test_login(username,password, expected):

    login_success = (
        username == VALID_USERNAME
        and password == VALID_PASSWORD
    )

    assert login_success == expected
#Pytest recognizes this as a test because of the test_ prefix.

def test_user_creation(test_user):
    assert test_user["username"] == "testuser"
    assert test_user["email"] == "test@example.com"


# @pytest.fixture
# def api_client():

#     client = APIClient(
#         "https://jsonplaceholder.typicode.com"
#     )

#     return client