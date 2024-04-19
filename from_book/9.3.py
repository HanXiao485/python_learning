class User:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def discribe_user(self):
        user_name = f'{self.first_name} {self.last_name}'
        print(user_name)

    def greet_user(self):
        print('Hello')

user_1 = User('Xiao', 'Han')
user_1.discribe_user()
user_1.greet_user()