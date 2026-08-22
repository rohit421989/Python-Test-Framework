class UserDataAPI:

    def __init__(self, api_client):

        self.api_client = api_client

    def get_user(self, user_id):

        return self.api_client.get(
            f"/users/{user_id}"
        )