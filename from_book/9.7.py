class User:
    def __init__(self, first_name, last_name):
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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can ban user','can delete cost']

    def show_privileges(self):
        print(self.privileges)

admin = Admin('Xiao', 'Han')
admin.show_privileges()