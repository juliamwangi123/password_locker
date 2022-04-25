

from pyrfc3339 import generate
from user import  User
from vault import Password_vault

def create_user(username,password):
    '''
    this function creates new users 
    '''
    new_user = User(username,password)
        
    return new_user


def save_user(user):
    '''
    this funtion saves new user 
    '''
    user.save_user()
    

def delete_user(user):
    
    """
    this functiondeletes a user
    
    """
    
    user.delete_user() 
    
    
def show_user():
    """
    this function show createsd and saves users
    """
    return User.show_user()
 
    
def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Password_vault.generatePassword()
    return auto_password 
    
  

def show():
    while True:
        print("Hello Welcome to your password vault select 'REG to Create New Account  'LI' to login into your accoutn")
        code=input("Enter code:..")
        if code == "REG":
            print("Create acount")
        username = input("Your Name: ")
        print("for automated passcode press 'auto' for custom password press 'cust' ")
        selection= input("Enter password selection:....")

        while True:
            if selection == 'cust':
                    password = input("Enter Password")
                    break
            elif selection == 'auto':
                    password = generate_Password()
                    break
            else:
                print("Invalid password please try again")
     
            
if __name__ == '__main__':

  show()

    
    
    
      
    