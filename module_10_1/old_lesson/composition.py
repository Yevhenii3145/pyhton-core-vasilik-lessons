class Car:
    """Common car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptiv_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometr(self):
        print("This car has " + str(self.odometr_reading) + " km")

    def update_odometr(self,kilometr):
        if kilometr >= self.odometr_reading:
            self.odometr_reading = kilometr
        else:
            print("You can't roll back an odometr")
    def increment_odometr(self,kilometr):
        self.odometr_reading += kilometr

    def fills_gas_tank(self):
        pass

class Battery():
    """This is a battery class."""
    def __init__(self, battery_size=20):
        self.battery_size = battery_size

    def get_describe_battery(self):
        """Print power the battery."""
        print("This car has a " + str(self.battery_size) + " -kwH battery")

    def get_range(self):
        """Aproximately range"""
        if self.battery_size == 20:
            range = 240
        elif self.battery_size == 100:
            range = 932
        message = "This car can go approximately " + str(range)
        message += " kilometer on a full  range"
        print(message)

class ElectricCar(Car):
    """Electric aspects of car"""
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery_power = Battery()

    def fills_gas_tank(self):
        print("Electric car don't need a tank")


my_electric_car = ElectricCar("nissan","leaf", 2018)
print(my_electric_car.get_descriptiv_name()) # 2018 nissan leaf


my_electric_car.battery_power.get_describe_battery() # This car has a 20 -kwH battery
my_electric_car.battery_power.get_range() # This car can go approximately 240 kilometer on a full  range
