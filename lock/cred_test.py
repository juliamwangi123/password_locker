import unittest

from vault import Password_vault

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for in password vault class

    """ 
    def setCreds(self):
        """
        Method creates an object from password vault and
        runs before the  other test case

        """
 
        self.new_credential = Password_vault('twitter','jules','1234')



    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.site,'twitter')
        self.assertEqual(self.new_credential.regesterdBy,'jules')
        self.assertEqual(self.new_credential.site_password,'1234')

    












if __name__ == '__main__':
    unittest.main()   

