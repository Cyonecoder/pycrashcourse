# from car import Car, ElectricCar
import car

# my_tesla = ElectricCar("tesla", "model s", 2019)
# print(my_tesla.get_descriptive_name())

# my_beetle = Car("volkswagen", "beetle", 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar("tesla", "roadster", 2020)

# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


my_tesla = car.Car("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())
my_mercedes = car.Car("Mercdes", "Gle", 2026)
print(my_mercedes.get_descriptive_name())
