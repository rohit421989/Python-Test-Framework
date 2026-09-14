import pytest

from framework.ai.openai_llm_client import OpenAILLMClient
from framework.ai.llm_response_validator import LLMResponseValidator


@pytest.mark.ai
@pytest.mark.live_ai
def test_real_llm_response():

    client = OpenAILLMClient()

    result = client.generate(
        "Reply with exactly one word: testing"
    )

    LLMResponseValidator.assert_not_empty(result)
    LLMResponseValidator.assert_token_limit(
        result,
        100
    )

    assert "testing" in result.response.lower()