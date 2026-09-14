# import os
# import time

# from openai import OpenAI

# from framework.ai.llm_client import LLMClient
# from framework.ai.llm_response import LLMResponse


# class OpenAILLMClient(LLMClient):

#     def __init__(self):
#         api_key = os.getenv("OPENAI_API_KEY")

#         if not api_key:
#             raise ValueError(
#                 "OPENAI_API_KEY environment variable is not configured."
#             )

#         self.client = OpenAI(api_key=api_key)

#     def generate(self, prompt: str):

#         start_time = time.perf_counter()

#         response = self.client.responses.create(
#             model="gpt-5.6-mini",
#             input=prompt
#         )

#         latency_ms = (
#             time.perf_counter() - start_time
#         ) * 1000

#         return LLMResponse(
#             prompt=prompt,
#             response=response.output_text,
#             model=response.model,
#             tokens=response.usage.total_tokens,
#             latency_ms=latency_ms
#         )


import time

from openai import OpenAI

from config.ai_config import AIConfig
from framework.ai.llm_client import LLMClient
from framework.ai.llm_response import LLMResponse
from framework.exceptions.framework_exceptions import ConfigurationException


class OpenAILLMClient(LLMClient):

    def __init__(self):

        if not AIConfig.OPENAI_API_KEY:
            raise ConfigurationException(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(
            api_key=AIConfig.OPENAI_API_KEY
        )

    def generate(self, prompt: str):

        start_time = time.perf_counter()

        response = self.client.responses.create(
            model=AIConfig.OPENAI_MODEL,
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