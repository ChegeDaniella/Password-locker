import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):

    def setUp(self):
        
        self.new_credential= Credentials("chege","123","chege@gmail.com")

    def tearDown(self):

        Credentials.credentials_list=[]

    def test_init(self):

        self.assertEqual(self.new_credential.username,"chege")
        self.assertEqual(self.new_credential.password,"123")
        self.assertEqual(self.new_credential.email,"chege@gmail.com")

    def test_save_credentials(self):

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):

        self.new_credential.save_credentials()
        test_credential = Credentials("Test","321","chege@gmail.com")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)    
        

    # def test_random_password(self):

    #     self.new_credential.generate_password() 
    #     self.assertEqual(self.new_credential.password,"") 

    def test_find_by_username(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Test","0711","test@user.com") # new contact
        test_credential.save_credentials()

        found_credential = Credentials.find_by_username("Test")

        self.assertEqual(found_credential.password,test_credential.password)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Test","0711","test@user.com") # new contact
        test_credential.save_credentials()

        credential_exists = Credentials.credential_exist("0711")    

if __name__ == '__main__':
    unittest.main()    
