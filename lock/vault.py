#this class will create password vault
class Password_vault:
    accounts_password= []

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
        
          