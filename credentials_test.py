import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):

    def setUp(self):
        
        self.new_credential= Credentials("chege","123")

    def tearDown(self):

        Credentials.credentials_list=[]

    def test_init(self):

        self.assertEqual(self.new_credential.username,"chege")
        self.assertEqual(self.new_credential.password,"123")

    def test_save_credentials(self):

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):

        self.new_credential.save_credentials()
        test_credential = Credentials("Test","321")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)    
        

    def test_random_password(self):

        self.new_credential.generate_password() 
        self.assertEqual(self.new_credential.password,"") 

if __name__ == '__main__':
    unittest.main()    
