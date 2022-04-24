import unittest

from vault import Password_vault

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for in password vault class

    """ 
    def setUp(self):
        """
        Method creates an object from password vault and
        runs before the  other test case

        """
 
        self.new_credential = Password_vault('twitter','jules','1234')



















if __name__ == '__main___':
       unittest.main()