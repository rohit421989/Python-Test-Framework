import os


class ExecutionConfig:

    WORKERS = os.getenv(
        "PYTEST_WORKERS",
        "2"
    )