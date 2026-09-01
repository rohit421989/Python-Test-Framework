class UserService:

    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id):
        return self.api_client.get(
            f"/users/{user_id}"
        )

    def get_users(self):
        return self.api_client.get(
            "/users"
        )

    def create_user(self, user_data):
        return self.api_client.post(
            "/users",
            data=user_data
        )

    def delete_user(self, user_id):
        return self.api_client.delete(
            f"/users/{user_id}"
        )