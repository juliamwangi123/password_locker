from user import  User

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
 
    
    
    
  
     
    
    
    
      
    