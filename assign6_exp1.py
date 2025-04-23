"""Write a class called Password_manager. The class should have a list called old_passwords that
holds all of the user past passwords. The last item of the list is the user  current pass word.
There should be a method called get_password that returns the current password and a method
called set_password that sets the user password. The set_password method should only
change the password if the attempted password is different from all the user past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or
False depending on whether the string is equal to the current password or not."""

""""""

class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False 

    def is_correct(self, password):
        return password == self.get_password()


pm = PasswordManager()
password = input("Enter the password: ")
print(pm.set_password(password))
print(pm.get_password()) 


password_input = input("Enter the password: ")
print(pm.is_correct(password_input))
