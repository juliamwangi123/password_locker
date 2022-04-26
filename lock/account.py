
from user import  User
from credentials import Password_vault

def create_user(username,password):
    '''
    this function creates new users 
    '''
    new_user = User(username,password)
        
    return new_user



def save_new_user(User):
    '''
    this funtion saves new user 
    '''
    User.save_new_user()
    

def delete_user_detail(User):
    
    """
    this functiondeletes a user
    
    """
    
    User.delete_user() 
    
    
def show_user():
    """
    this function show createsd and saves users
    """
    return User.show_users_detail()
 

def userLogin(name, password):

    verifiedUserAccount = Password_vault.userVerification(name, password)

    return verifiedUserAccount

# credentials class method begin here

def createNewusercredential(site, regesterdBy, site_password):

    newUserCredential = Password_vault(site, regesterdBy, site_password)    
    return newUserCredential

def saveUserCredential(Password_vault):

    Password_vault.save_credentials()

def delCredential(Password_vault):

    Password_vault.delete_credentials() 
  
def displayUserCredentials():

    return Password_vault.display_credentials()
def findUserCredentials(site):

    return Password_vault.if_credential_exist(site)

# def doCredentialsExist(account):

#     return Password_vault.if_credential_exist(account)

def systemGeneratedPassword():

    autoGenRandPass = Password_vault.generatePassword()
    return autoGenRandPass


def show():

    print("WELCOME TO PASSWORD LOCKER")
    print("Please enter your name")
    username= input()
    print(f"Hi {username}, use the following codes to get you started")
    print(">>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>")

    print("RE: To create a new account")
    print("LO: To  login into your account")
    comands= input().upper().strip()
    
    if comands == "RE":
        print(">>>>>>>>>>>>>>>>>>>>>>")

        print("Enter Your First Name: ")
        name = input()
       
        
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>")

            print("CS: To enter your password")
            print("GP: To generate password")
            command= input().upper().strip()

            if command == "CS":
                print(">>>>>>>>>>>>>>>>>>>>>>")

                print("PLease enter password: ")
                login_pass= input()
                break

            elif command == "GP":

                login_pass= systemGeneratedPassword()
                break

            else:

                print("Please select a valid option")
       

        save_new_user(create_user(name,login_pass))
        print(f" Thank you {username}. You have successfully signed up ")
        show_user()

        print(">>>>>>>>>>>>>>>>>>>>>>")
# Login  into account
    elif comands =="LO":
        
        print("Enter username and password to sign in: ")
        username= input("Username:  ")
        login_pass= input("Password:  ")
        userlogins = userLogin(username,login_pass)
        
        if userLogin == userlogins:
            print(f"Hi, {username}. Welcome back to Password Vault")

    while True:
        print(">>>>>>>>>>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>>>>>>>>>>")
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
                    print(f"your generated passcode is {password}")
                    break

                else:
                    print(" Incorrect command choice. Try again")

            saveUserCredential(createNewusercredential(userAccountName,accUsername,password))
            print(f"Credential for {userAccountName}  Username: {accUsername} and Password: {password} have been successfully")

        elif command == "DC" :

            if displayUserCredentials():

                print("Account Exist: ")

                # for acc in displayUserCredentials():
                for Password_vault in displayUserCredentials():
                    print(f"Account: {Password_vault.site}")
                    print(f"Username: {Password_vault.regesterdBy}")
                    print(f"Password: {Password_vault.site_password}")


            else:

                print("Error! The entered credentials do not exist! ")

        elif command == "FC":

            print("Search account : ")
            accountName = input()

            if findUserCredentials(accountName):

                searchAcc = findUserCredentials(accountName)
                print(f"Account : {searchAcc} \n")
                # print(f"Username: { searchAcc} \n")

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
                print("searchAcc")
                # searchAcc.delCredential()
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

    
    
    
      
    