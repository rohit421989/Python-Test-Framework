class ResponseValidator:

    @staticmethod
    def assert_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status code {expected_status}, "
            f"but received {response.status_code}. "
            f"Response: {response.text}"
        )

    @staticmethod
    def assert_response_not_empty(response):
        data = response.json()

        assert data, (
            "Expected response body to contain data, "
            "but response was empty."
        )

    @staticmethod
    def assert_field_exists(response, field):
        data = response.json()

        assert field in data, (
            f"Expected field '{field}' in response. "
            f"Actual response: {data}"
        )

    @staticmethod
    def assert_field_value(response, field, expected_value):
        data = response.json()

        assert field in data, (
            f"Field '{field}' was not found in response."
        )

        assert data[field] == expected_value, (
            f"Expected '{field}' to be '{expected_value}', "
            f"but received '{data[field]}'."
        )