import requests
from framework.logging.logger import Logger

class APIClient:

    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout

        self.logger = Logger.get_logger(
            self.__class__.__name__
        )

    def set_auth_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"    

    def get(self, endpoint, headers=None, params=None):

        request_headers = {
            **self.headers,
            **(headers or {})
        }

        self.logger.info(
            f"GET request: {endpoint}"
        )

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=request_headers,
            params=params,
            timeout=self.timeout
        )

        self.logger.info(
            f"Response status: {response.status_code}"
        )
        return response

    def post(self, endpoint, data=None, headers=None):

        request_headers = {
            **self.headers,
            **(headers or {})
        }

        self.logger.info(
            f"POST request: {endpoint}"
        )

        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=request_headers,
            timeout=self.timeout
        )

        self.logger.info(
            f"Response status: {response.status_code}"
        )
        return response

    def put(self, endpoint, data=None, headers=None):

        request_headers = {
            **self.headers,
            **(headers or {})
        }

        return requests.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=request_headers,
            timeout=self.timeout
        )

    def patch(self, endpoint, data=None, headers=None):

        request_headers = {
            **self.headers,
            **(headers or {})
        }

        return requests.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=request_headers,
            timeout=self.timeout
        )

    def delete(self, endpoint, headers=None):

        request_headers = {
            **self.headers,
            **(headers or {})
        }

        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=request_headers,
            timeout=self.timeout
        )