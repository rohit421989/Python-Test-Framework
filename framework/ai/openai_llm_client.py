import os
import time

from openai import OpenAI

from framework.ai.llm_client import LLMClient
from framework.ai.llm_response import LLMResponse


class OpenAILLMClient(LLMClient):

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not configured."
            )

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str):

        start_time = time.perf_counter()

        response = self.client.responses.create(
            model="gpt-5.6-mini",
            input=prompt
        )

        latency_ms = (
            time.perf_counter() - start_time
        ) * 1000

        return LLMResponse(
            prompt=prompt,
            response=response.output_text,
            model=response.model,
            tokens=response.usage.total_tokens,
            latency_ms=latency_ms
        )