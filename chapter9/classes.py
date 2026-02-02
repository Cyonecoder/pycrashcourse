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
