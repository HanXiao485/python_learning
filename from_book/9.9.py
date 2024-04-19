class Car:

    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('stop')

    def increament_odometer(self,miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self,battery_size = 40) -> None:
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-KWh battery.')

    def get_upgrade(self):

        if self.battery_size ==40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f'This can can go about {range} miles on the full charge.')

    def get_range(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()

    

my_leaf = ElectricCar('nissan','leaf','2024')

print(my_leaf.battery.battery_size)

my_leaf.battery.get_range()

print(my_leaf.battery.battery_size)
my_leaf.battery.get_upgrade()
