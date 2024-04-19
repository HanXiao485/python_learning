class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name},{self.cuisine_type}')

    def open_restaurant(self):
        print('open')

    def served(self):
        print(f'{self.number_served}')
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type,) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']


icecream = IceCreamStand('Han', 'china')
print(icecream.flavors)