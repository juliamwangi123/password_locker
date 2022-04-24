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
 
    
    
    
  

def show():
    
    while True:
        print("To Register click 'REG' to login 'LOG' ")

        code = input().upper()
        print()
        print()
        
        
        if code == 'REG':
            
            print("Enter Username:")
            username = input()
            
            print("Create your Password")
            password= input()
            
            print("Confirm your Password")
            confirm_password = input()
            
            if confirm_password != password:
                print("Your password did not match.Try Again")
                password = input()
                print("Confirm Your password")
                confirm_password = input()
                
            else:
                print("Succesfully Registerd")
                print("LOGIN")
                print("Enter your Username")
                name = input()
                print("Enter Password")
                user_pass= input()
                
                
            while name != username or user_pass != password:
                print("Your Username or Password is invalid")
                print("Re-enter your Username")
                name = input()
                print("Enter your Password")
                user_pass = input()
                
            else:
                print(" you've logged in succesfully")
                
        elif code == 'L0G':
            print("Welcome, Login to your Account")
            print("Enter your Username")
            saved_username = input()
            print("Enter Password")
            saved_password = input()
            
            if saved_username != "jules" or saved_password != "test":
                 print("Invalid username or password. Username is 'jules' and Password is 'test'")
                 print("Enter your Username")
                 saved_username= input()
                 print("Enter Password")
                 saved_password = input()
                 
            else:
                print("Logged in Succesfully")
                
                
        
        elif code == 'EXIT':
            break
        
        else:
            
            print("We did not recgnize the code picked")  
            
            
if __name__ == '__main__':



    
    
    
      
    