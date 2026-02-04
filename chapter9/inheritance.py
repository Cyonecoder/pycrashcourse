class Car:
    """A simple attemt to represent a car."""

    model: str = ""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.odometer_reading} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, mileage):
        """set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back on odometer")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()

    def fill_gas_tank(self):
        print("this car doesn't need a gas tank")


my_tesla = ElectricCar("tesla", "Model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery = Battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
