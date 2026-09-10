# import pytest

# from framework.ai.mock_llm_client import MockLLMClient


# @pytest.mark.ai
# def test_llm_generates_response():

#     client = MockLLMClient()

#     result = client.generate(
#         "What is software testing?"
#     )

#     assert result is not None
#     assert result["response"]
#     assert result["model"] == "mock-model"
#     assert result["tokens"] > 0

# import pytest

# from framework.ai.mock_llm_client import MockLLMClient
# from framework.ai.llm_response import LLMResponse


# @pytest.mark.ai
# def test_llm_generates_response():

#     client = MockLLMClient()

#     result = client.generate(
#         "What is software testing?"
#     )

#     assert isinstance(result, LLMResponse)

#     assert result.response
#     assert result.model == "mock-model"
#     assert result.tokens > 0
#     assert result.latency_ms >= 0

import pytest

from framework.ai.mock_llm_client import MockLLMClient
from framework.ai.llm_response import LLMResponse
from framework.ai.llm_response_validator import LLMResponseValidator


@pytest.mark.ai
def test_llm_generates_response():

    client = MockLLMClient()

    result = client.generate(
        "What is software testing?"
    )

    assert isinstance(result, LLMResponse)

    LLMResponseValidator.assert_not_empty(result)
    LLMResponseValidator.assert_model(
        result,
        "mock-model"
    )
    LLMResponseValidator.assert_token_limit(
        result,
        100
    )
    LLMResponseValidator.assert_latency(
        result,
        1000
    )

@pytest.mark.ai
def test_software_testing_response():

    client = MockLLMClient()

    result = client.generate(
        "What is software testing?"
    )

    LLMResponseValidator.assert_contains_keyword(
        result,
        "validating"
    )


@pytest.mark.ai
def test_capital_of_india_response():

    client = MockLLMClient()

    result = client.generate(
        "What is the capital of India?"
    )

    LLMResponseValidator.assert_contains_keyword(
        result,
        "New Delhi"
    )


@pytest.mark.ai
def test_software_testing_response():

    client = MockLLMClient()

    result = client.generate(
        "What is software testing?"
    )

    LLMResponseValidator.assert_contains_keyword(
        result,
        "validating"
    )


@pytest.mark.ai
def test_capital_of_india_response():

    client = MockLLMClient()

    result = client.generate(
        "What is the capital of India?"
    )

    LLMResponseValidator.assert_contains_keyword(
        result,
        "New Delhi"
    )