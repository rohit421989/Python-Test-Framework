import json

from attrs import field


class JSONResponseValidator:

    @staticmethod
    def parse_json(response_text):
        try:
            return json.loads(response_text)
        except json.JSONDecodeError as error:
            raise AssertionError(
                f"LLM response is not valid JSON: {response_text}"
            ) from error

    @staticmethod
    def assert_required_fields(data, required_fields):

        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        assert not missing_fields, (
            f"Missing required fields: {missing_fields}. "
            f"Actual response: {data}"
        )


    @staticmethod
    def assert_field_types(data, expected_types):

        type_errors = []

        for field, expected_type in expected_types.items():

            if field not in data:
                type_errors.append(
                    f"Missing field '{field}'"
                )
                continue

            if not isinstance(data[field], expected_type):
                type_errors.append(
                    f"Field '{field}' expected "
                    f"{expected_type.__name__}, "
                    f"but received {type(data[field]).__name__}"
                )

        assert not type_errors, (
            "Type validation failed: "
            + "; ".join(type_errors)
        )  

    @staticmethod
    def assert_value_in_range(data, field, min_value, max_value):

        assert field in data, (
            f"Field '{field}' is missing."
        )

        value = data[field]

        assert min_value <= value <= max_value, (
            f"Field '{field}' expected value between "
            f"{min_value} and {max_value}, "
            f"but received {value}."
        )


    @staticmethod
    def assert_value_in_allowed_values(data, field, allowed_values):

        assert field in data, (
            f"Field '{field}' is missing."
        )

        value = data[field]

        assert value in allowed_values, (
            f"Field '{field}' expected one of "
            f"{allowed_values}, but received '{value}'."
        )      