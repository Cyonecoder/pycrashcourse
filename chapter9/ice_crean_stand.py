from chapter9.admin import Admin
from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["choco", "pstaccia", "vanilla", "raseberry"]

    def display_flavors(self):
        print(f"flavors :{self.flavors}")


creamy = IceCreamStand("IbiCream", "Patesserie")

creamy.display_flavors()


useradmin = Admin("Chams", "Kilowa", "chams@kilo.com", 1999, "tiznit")
useradmin.show_privileges()
