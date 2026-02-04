from privileges import Privileges
from users import User


class Admin(User):

    def __init__(self, first_name, last_name, email, date_of_birth, location):
        super().__init__(first_name, last_name, email, date_of_birth, location)
        self.privileges = Privileges()

    def show_privileges(self):
        print(
            f"User {self.first_name} has the privileges :{self.privileges.privileges}"
        )
