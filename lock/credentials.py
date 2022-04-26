#this class will create password vault
import string
import random
from traceback import print_stack
from user import User
class Password_vault:
    accounts_password= []



    @classmethod
    def userVerification(cls, name, password):
       
        _user = " "
        for user in User.user_detail:
            if user.name == name and user.password ==password:
                _user == user.name
        return _user

    def __init__(self, site, regesterdBy, site_password):
        ''''
         add an instance properties  using the constructor
         '''
        self.site = site
        self.regesterdBy = regesterdBy
        self.site_password = site_password



    #create credentials for account
    def save_credentials(self):
        """
         this function creates new accounts in password vault
         """
        Password_vault.accounts_password.append(self)
    
    def delete_credentials(self):
        """
          this function to delets users account details from the password vault
         """
        
        Password_vault.accounts_password.remove(self)  
    
    
    
    @classmethod 
    def display_credentials(cls):
        """"
        this method show s all theaccounts and password inside password vaul
        
        """
        
        return cls.accounts_password
        
    
    @classmethod
    def find_credential(cls, site):
        """
        Method that takes in sites name and returns  password .

        """
        for password in cls.accounts_password:
            if password.site== site:
                return password
    
   
   
    @classmethod
    def if_credential_exist(cls, site):
        """
        this method checks if the sites credentials exist or not.
        """
        for credential in cls.accounts_password:
            if credential.site == site:
                return True
        return False

    def generatePassword(passLength=5):
        """Password random generator"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(passLength))

