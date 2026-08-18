import pytest

from framework.utilities.response_validator import (
    ResponseValidator
)


@pytest.mark.api
@pytest.mark.database
def test_user_api_and_database(
    api_client,
    db_client,
    clean_users_table
):

    # Create database table
    db_client.execute_update(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
        """
    )

    # Simulate application persistence
    db_client.execute_update(
        """
        INSERT INTO users (id, name, email)
        VALUES (1, 'Rohit', 'rohit@example.com')
        """
    )

    # Call API
    response = api_client.get("/users/1")

    ResponseValidator.assert_status_code(
        response,
        200
    )

    api_user = response.json()

    # Retrieve DB record
    db_result = db_client.execute_query(
        """
        SELECT id, name, email
        FROM users
        WHERE id = 1
        """
    )

    db_user = db_result[0]

    # Validate database
    assert db_user[0] == 1

    # Validate API/DB relationship
    assert api_user["id"] == db_user[0]