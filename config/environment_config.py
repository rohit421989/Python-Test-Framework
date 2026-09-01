import os


class EnvironmentConfig:
    ENVIRONMENT = os.getenv("TEST_ENV", "local").lower()

    IS_DOCKER = os.getenv("DOCKER_ENV", "false").lower() == "true"
    IS_CI = os.getenv("CI", "false").lower() == "true"

    @classmethod
    def is_local(cls):
        return cls.ENVIRONMENT == "local"

    @classmethod
    def is_docker(cls):
        return cls.IS_DOCKER

    @classmethod
    def is_ci(cls):
        return cls.IS_CI