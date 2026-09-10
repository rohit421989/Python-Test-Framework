class LLMResponseValidator:

    @staticmethod
    def assert_not_empty(response):
        assert response.response.strip(), (
            "LLM response should not be empty."
        )

    @staticmethod
    def assert_model(response, expected_model):
        assert response.model == expected_model, (
            f"Expected model '{expected_model}', "
            f"but received '{response.model}'."
        )

    @staticmethod
    def assert_token_limit(response, max_tokens):
        assert response.tokens <= max_tokens, (
            f"Expected token usage <= {max_tokens}, "
            f"but received {response.tokens}."
        )

    @staticmethod
    def assert_latency(response, max_latency_ms):
        assert response.latency_ms <= max_latency_ms, (
            f"Expected latency <= {max_latency_ms} ms, "
            f"but received {response.latency_ms} ms."
        )

    @staticmethod
    def assert_contains_keyword(response, keyword):
        assert keyword.lower() in response.response.lower(), (
            f"Expected response to contain keyword '{keyword}'. "
            f"Actual response: {response.response}"
        )