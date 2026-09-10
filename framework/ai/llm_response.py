from dataclasses import dataclass


@dataclass
class LLMResponse:
    prompt: str
    response: str
    model: str
    tokens: int
    latency_ms: float = 0.0