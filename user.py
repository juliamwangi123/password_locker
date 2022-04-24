class User:
    ''''
    add a class variable that hold user details
    '''
    user_detail = []

    ''''
    add an instance to the class using the constructor
    '''
    def __init__(self,username, password):
        self.username =username
        self.password =password
        