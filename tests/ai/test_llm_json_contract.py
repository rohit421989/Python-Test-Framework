import pytest

from framework.ai.json_response_validator import JSONResponseValidator
from framework.ai.llm_response import LLMResponse


@pytest.mark.ai
def test_llm_json_contract():

    response = LLMResponse(
        prompt="Return user details as JSON",
        response='{"name": "Test User", "role": "QA Engineer"}',
        model="mock-model",
        tokens=15,
        latency_ms=40
    )

    data = JSONResponseValidator.parse_json(
        response.response
    )

    JSONResponseValidator.assert_required_fields(
        data,
        ["name", "role"]
    )

    assert data["role"] == "QA Engineer"

@pytest.mark.ai
def test_invalid_json_response():

    invalid_response = """
    {
        "name": "Test User",
        "role": "QA Engineer"
    """

    with pytest.raises(
        AssertionError,
        match="LLM response is not valid JSON"
    ):
        JSONResponseValidator.parse_json(
            invalid_response
        )


@pytest.mark.ai
def test_missing_required_field():

    data = {
        "name": "Test User"
    }

    with pytest.raises(
        AssertionError,
        match="Missing required fields"
    ):
        JSONResponseValidator.assert_required_fields(
            data,
            ["name", "role"]
        )

@pytest.mark.ai
def test_llm_response_field_types():

    data = {
        "name": "Test User",
        "confidence": 0.92,
        "approved": True
    }

    JSONResponseValidator.assert_field_types(
        data,
        {
            "name": str,
            "confidence": float,
            "approved": bool
        }
    )


@pytest.mark.ai
def test_invalid_llm_response_field_types():

    data = {
        "name": "Test User",
        "confidence": "high",
        "approved": True
    }

    with pytest.raises(
        AssertionError,
        match="Type validation failed"
    ):
        JSONResponseValidator.assert_field_types(
            data,
            {
                "name": str,
                "confidence": float,
                "approved": bool
            }
        )


@pytest.mark.ai
def test_confidence_score_range():

    data = {
        "confidence": 0.87
    }

    JSONResponseValidator.assert_value_in_range(
        data,
        "confidence",
        0.0,
        1.0
    )


@pytest.mark.ai
def test_invalid_confidence_score():

    data = {
        "confidence": 1.4
    }

    with pytest.raises(
        AssertionError,
        match="expected value between"
    ):
        JSONResponseValidator.assert_value_in_range(
            data,
            "confidence",
            0.0,
            1.0
        )


@pytest.mark.ai
def test_allowed_classification_value():

    data = {
        "classification": "safe"
    }

    JSONResponseValidator.assert_value_in_allowed_values(
        data,
        "classification",
        ["safe", "unsafe", "unknown"]
    )


@pytest.mark.ai
def test_invalid_classification_value():

    data = {
        "classification": "maybe"
    }

    with pytest.raises(
        AssertionError,
        match="expected one of"
    ):
        JSONResponseValidator.assert_value_in_allowed_values(
            data,
            "classification",
            ["safe", "unsafe", "unknown"]
        )                        