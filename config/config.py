import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    ENVIRONMENT = os.getenv("TEST_ENV", "qa")

    API_USERNAME = os.getenv("API_USERNAME")
    API_PASSWORD = os.getenv("API_PASSWORD")
    API_TOKEN = os.getenv("API_TOKEN")

    BASE_URLS = {
        "dev": "https://jsonplaceholder.typicode.com",
        "qa": "https://jsonplaceholder.typicode.com",
        "staging": "https://jsonplaceholder.typicode.com",
    }

    @classmethod
    def get_base_url(cls):
        return cls.BASE_URLS.get(cls.ENVIRONMENT)