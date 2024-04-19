class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}, {self.cuisine_type}')

    def open_restaurant(self):
        print('open')


restaurant_1 = Restaurant('num_1', 'china')
restaurant_2 = Restaurant('num_2', 'german')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()