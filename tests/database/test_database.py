import pytest


@pytest.mark.database
def test_database_connection(db_client):

    result = db_client.execute_query(
        "SELECT 1"
    )

    assert result[0][0] == 1


@pytest.mark.database
def test_create_user(
    db_client,
    clean_users_table
):

    db_client.execute_update(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
        """
    )

    db_client.execute_update(
        """
        INSERT INTO users (id, name, email)
        VALUES (1, 'Rohit', 'rohit@example.com')
        """
    )

    result = db_client.execute_query(
        "SELECT * FROM users WHERE id = 1"
    )

    assert result[0][1] == "Rohit"
    assert result[0][2] == "rohit@example.com"