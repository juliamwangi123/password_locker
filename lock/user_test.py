import unittest

from user import User  # Importing the User and Credentials class



class TestUser(unittest.TestCase):
    
  
    
    def setUp(self):
        
        '''
        this method runs before other test case method
        this method creates an object from the class user
        '''
        self.new_user = User("jules","1234") 

    def test_properties(self):
        '''
        this method checks if the objects property are
        correctly initialized
        '''
        self.assertEqual(self.new_user.username,'jules')
        self.assertEqual(self.new_user.password,'123')
