import pytest

from framework.utilities.response_validator import ResponseValidator
from framework.api.schemas.user_schema import UserSchema

@pytest.mark.api
def test_get_users(api_client):

    response = api_client.get("/users")

    ResponseValidator.assert_status_code(
        response,
        200
    )

    users = response.json()
    assert len(users) > 0

@pytest.mark.api
def test_create_user(api_client):

    user_data = {
        "name": "Rohit",
        "username": "rohit123",
        "email": "rohit@example.com"
    }

    response = api_client.post(
        "/users",
        data=user_data
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == "Rohit"
    assert response_data["username"] == "rohit123"    

@pytest.mark.api
def test_delete_user(api_client):

    response = api_client.delete("/users/1")

    assert response.status_code == 200    