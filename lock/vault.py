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