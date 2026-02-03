class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a commad."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over !")


mydog = Dog("rocky", 3)
your_dog = Dog("maya", 4)
mydog.sit()
mydog.roll_over()
print(mydog.name)

your_dog.sit()
your_dog.roll_over()
print(your_dog.name)


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name} cook's {self.cuisine_type} food ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open")


salome = Restaurant("Salome Marina", "Ocean/Asian")
salome.describe_restaurant()
salome.open_restaurant()
salome = Restaurant("Pizza Napolitano", "Italian")
salome.describe_restaurant()
salome = Restaurant("El Marrakech", "Morocan")
salome.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, email, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.location = location

    def describe_user(self):
        print(
            f"User: {self.first_name+" "+self.last_name} born in {self.date_of_birth} located in {self.location}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name}")


user1 = User("hamid", "smires", "hamid.smires@gg.co", 1990, "lalaland")
user2 = User("karima", "kiki", "kiki.ma@fo.com", 1990, "llulucity")
user3 = User("nada", "3bi9a", "nana.3bi@dd.ha", 1990, "hozlofik")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
