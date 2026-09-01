class UserBuilder:

    @staticmethod
    def valid_user():
        return {
            "name": "Test User",
            "username": "testuser",
            "email": "testuser@example.com"
        }

    @staticmethod
    def user_with_email(email):
        user = UserBuilder.valid_user()
        user["email"] = email
        return user

    @staticmethod
    def user_with_username(username):
        user = UserBuilder.valid_user()
        user["username"] = username
        return user