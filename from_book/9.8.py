class Privileges:

    def __init__(self):
        self.privileges = ['can ban user','can delete cost']
    
    def show_privileges(self):
        print(f'{self.privileges}')

class Admin:

    def __init__(self):
        self.privileges = Privileges()

admin = Admin()
admin.privileges.show_privileges()