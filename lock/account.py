

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

def userLogin(name, password):

    verifiedUserAccount = Password_vault.userVerification(name, password)

    return verifiedUserAccount


def createNewusercredential( siteName, username,password):

    newUserCredential = Password_vault(siteName, username,password)    
    return newUserCredential

def saveUserCredential(userCredential):

    userCredential.save_credentials()

def delCredential(credentials):

    credentials.delete_credentials()
  
def displayUserCredentials():

    return Password_vault.display_credentials()
def findUserCredentials(userAccount):

    return Password_vault.find_credential(userAccount)

def doCredentialsExist(account):

    return Password_vault.if_credential_exist(account)

def systemGeneratedPassword():

    autoGenRandPass = Password_vault.generatePassword()
    return autoGenRandPass


def show():

    print("WELCOME TO PASSWOD LOCKER")
    print("Please enter your name")
    username= input()
    print(f"Hi {username}, use the following codes to get you started")
    print("RE: To create a new account")
    print("LO: To  login into your account")
    comands= input().upper().strip()
    
    if comands == "RE":

        print("Enter Your First Name: ")
        name = input()
       
        
        while True:

            print("CS: To enter your password")
            print("GP: To generate password")
            command= input().upper().strip()

            if command == "CS":

                print("PLease enter password: ")
                login_pass= input()
                break

            elif command == "GP":

                login_pass= generate_Password()
                break

            else:

                print("Please select a valid option")

        save_user(create_user(name,login_pass))
        print(f" Thank you {username}. You have successfully signed up ")
        show_user()()

    elif comands =="LO":

        print("Enter username and password to sign in: ")
        username= input("Username:  ")
        login_pass= input("Password:  ")
        userlogins = userLogin(username,login_pass)
        if userLogin == userlogins:
            print(f"Hi, {username}. Welcome back to Password Vault")

    while True:

        print("Please key in any of the following to proceed ")
        print("CC: Create new user Credential")
        print("DC: Display existing Account credentials")
        print("FC: Find User Credential")
        print("GP: Auto generated Password")
        print("DEL: Delete account credential")
        print("X: Exit application")

        command= input().upper().strip()

        if command == "CC":

            print("Create new user Account Credential")
            print("Enter account Name : ")
            userAccountName = input().upper().strip()

            print("Username for above account")
            accUsername =input().strip()

            while True:

                print("1 - Type Password ")
                print("2 - Use system Generated Password")
                p_choice= input().strip()

                if p_choice == "1":

                    print("Type Password : ")
                    password = input()
                    break

                elif p_choice == "2":

                    password= systemGeneratedPassword()
                    break

                else:
                    print(" Incorrect command choice. Try again")

            saveUserCredential(createNewusercredential(userAccountName,accUsername,password))
            print(f"Credential for {userAccountName}  Username: {accUsername} and Password: {password} have been successfully")

        elif command == "DC" :

            if displayUserCredentials():

                print("Account Exist: ")

                for acc in displayUserCredentials():

                    print(f"Account: {acc.myAccount}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")


            else:

                print("Error! The entered credentials do not exist! ")

        elif command == "FC":

            print("Sarch account : ")
            accountName = input().upper().strip

            if findUserCredentials(accountName):

                searchAcc = findUserCredentials(accountName)
                print(f"Account : {searchAcc.myAccount} \n")
                print(f"Username: { searchAcc.username} \n")

            else:

                print(f"accountName doesnt exist \n")

        elif command == "GP":

            password = systemGeneratedPassword()
            print(f"Your generated password is : {password}")

        elif command == "DEL":

            print("Enter Account to Delete ")
            accountName = input().upper().strip()

            if findUserCredentials(accountName):

                searchAcc = findUserCredentials(accountName)
                print("")
                searchAcc.delCredential()
                print(f"{ searchAcc.myAccount} deleted successfully \n")

            else:

                print(f"{accountName} The account does not exist \n")

        elif command == "X":

            print("Exit....\n")
            break

        else:

            print(" enter a valid command!")



            
if __name__ == '__main__':

  show()

    
    
    
      
    