from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Base interface for all LLM clients.
    """

    @abstractmethod
    def generate(self, prompt: str):
        """
        Send a prompt to an LLM and return the response.
        """
        pass