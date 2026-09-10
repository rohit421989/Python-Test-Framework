# from framework.ai.llm_client import LLMClient


# class MockLLMClient(LLMClient):

#     def generate(self, prompt: str):

#         return {
#             "prompt": prompt,
#             "response": "This is a mock LLM response.",
#             "model": "mock-model",
#             "tokens": 10
#         }


# from framework.ai.llm_client import LLMClient
# from framework.ai.llm_response import LLMResponse


# class MockLLMClient(LLMClient):

#     def generate(self, prompt: str):

#         return LLMResponse(
#             prompt=prompt,
#             response="This is a mock LLM response.",
#             model="mock-model",
#             tokens=10,
#             latency_ms=50.0
#         )


# from framework.ai.llm_client import LLMClient
# from framework.ai.llm_response import LLMResponse


# class MockLLMClient(LLMClient):

#     def generate(self, prompt: str):

#         prompt_lower = prompt.lower()

#         if "software testing" in prompt_lower:
#             response_text = (
#                 "Software testing is the process of validating "
#                 "that software behaves as expected."
#             )

#         elif "capital of india" in prompt_lower:
#             response_text = "The capital of India is New Delhi."

#         else:
#             response_text = "This is a generic mock LLM response."

#         return LLMResponse(
#             prompt=prompt,
#             response=response_text,
#             model="mock-model",
#             tokens=20,
#             latency_ms=50.0
#         )


from framework.ai.llm_client import LLMClient
from framework.ai.llm_response import LLMResponse


class MockLLMClient(LLMClient):

    def generate(self, prompt: str):

        prompt_lower = prompt.lower()

        if "software testing" in prompt_lower:
            response_text = (
                "Software testing is the process of validating "
                "that software behaves as expected."
            )

        elif "capital of india" in prompt_lower:
            response_text = "The capital of India is New Delhi."

        else:
            response_text = "This is a generic mock LLM response."

        return LLMResponse(
            prompt=prompt,
            response=response_text,
            model="mock-model",
            tokens=20,
            latency_ms=50.0
        )