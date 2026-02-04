from users import User

# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         """simulate a dog sitting in response to a commad."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over !")


# mydog = Dog("rocky", 3)
# your_dog = Dog("maya", 4)
# mydog.sit()
# mydog.roll_over()
# print(mydog.name)

# your_dog.sit()
# your_dog.roll_over()
# print(your_dog.name)


# salome = Restaurant("Salome Marina", "Ocean/Asian")
# salome.describe_restaurant()
# salome.open_restaurant()
# salome = Restaurant("Pizza Napolitano", "Italian")
# salome.describe_restaurant()
# salome = Restaurant("El Marrakech", "Morocan")
# salome.describe_restaurant()


# user1 = User("hamid", "smires", "hamid.smires@gg.co", 1990, "lalaland")
# user2 = User("karima", "kiki", "kiki.ma@fo.com", 1990, "llulucity")
# user3 = User("nada", "3bi9a", "nana.3bi@dd.ha", 1990, "hozlofik")

# user1.describe_user()
# user1.greet_user()
# user2.describe_user()
# user2.greet_user()
# user3.describe_user()
# user3.greet_user()


# class Car:
#     """A simple attemt to represent a car."""

#     model: str = ""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.odometer_reading} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def set_odometer(self, mileage):
#         """set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cant roll back on odometer")

#     def increment_odometer(self, mileage):
#         self.odometer_reading += mileage


# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.set_odometer(20)
# my_new_car.read_odometer()
# my_new_car.set_odometer(53)
# my_new_car.read_odometer()

# my_used_car = Car("subaru", "outback", 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.set_odometer(23_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# salome = Restaurant("Salome Marina", "Ocean/Asian")
# salome.describe_restaurant()
# salome.number_served = 2000
# print(salome.number_served)
# salome.set_number_served(3000)
# print(salome.number_served)
# salome.increment_number_served(400)
# print(salome.number_served)

user1 = User("hamid", "smires", "hamid.smires@gg.co", 1990, "lalaland")
user1.increment_login_attempt()
print(user1.login_attempt)
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print(user1.login_attempt)
user1.reset_login_attempts()
print(user1.login_attempt)
