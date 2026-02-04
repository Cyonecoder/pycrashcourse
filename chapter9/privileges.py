class Privileges:
    def __init__(self, privileges: list = None):
        if privileges:

            self.privileges = privileges
        else:
            self.privileges = ["add post", "can delete post", "can ban user"]

    def get_privileges(self):
        return self.privileges
