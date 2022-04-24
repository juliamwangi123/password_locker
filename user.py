class User:
    ''''
    add a class variable that hold user details
    '''
    user_detail = []

    
    def __init__(self,username, password):
        ''''
        add an instance properties  using the constructor
        '''
        self.username =username
        self.password =password
    
    def save_user(self):
        """
        add  new user to the list using append method
        """
        User.user_detail.append(self)
    