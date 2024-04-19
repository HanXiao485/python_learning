class User:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def discribe_user(self):
        user_name = f'{self.first_name} {self.last_name}'
        print(user_name)

    def greet_user(self):
        print('Hello')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('Xiao', 'Han')

print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
