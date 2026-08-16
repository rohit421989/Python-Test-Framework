class ResponseValidator:

    @staticmethod
    def assert_status_code(response, expected_status_code):

        actual_status_code = response.status_code

        assert actual_status_code == expected_status_code, (
            f"Expected status code "
            f"{expected_status_code}, "
            f"but received {actual_status_code}"
        )

    @staticmethod
    def assert_json_field(response, field, expected_value):

        response_data = response.json()

        actual_value = response_data.get(field)

        assert actual_value == expected_value, (
            f"Expected '{field}' to be "
            f"'{expected_value}', "
            f"but received '{actual_value}'"
        )