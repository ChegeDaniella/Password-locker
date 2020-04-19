import unittest
from user import User

class TestUser(unittest.TestCase):
    def tearDown(self):

        User.user_list=[]

    def setUp(self):

        self.new_user= User("chege","123")

    def test_init(self):

        self.assertEqual(self.new_user.username,"chege")
        self.assertEqual(self.new_user.password,"123")
        

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):

        self.new_user.save_user()
        test_user = User("chege","123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    # def test_find_user(self):

    #     self.new_user.save_user()
    #     test_user = User("Test","321")
    #     test_user.save_user()


if __name__ == '__main__':
    unittest.main()    
