from classes import Restaurant
from classes import User


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["choco", "pstaccia", "vanilla", "raseberry"]

    def display_flavors(self):
        print(f"flavors :{self.flavors}")


creamy = IceCreamStand("IbiCream", "Patesserie")

creamy.display_flavors()


class Admin(User):

    def __init__(self, first_name, last_name, email, date_of_birth, location):
        super().__init__(first_name, last_name, email, date_of_birth, location)
        self.privileges = ["add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"User {self.first_name} has the privileges :{self.privileges}")


useradmin = Admin("Chams", "Kilowa", "chams@kilo.com", 1999, "tiznit")
useradmin.show_privileges()
