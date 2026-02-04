class User:
    def __init__(self, first_name, last_name, email, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempt = 0

    def describe_user(self):
        print(
            f"User: {self.first_name} {self.last_name} born in {self.date_of_birth} located in {self.location}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0
