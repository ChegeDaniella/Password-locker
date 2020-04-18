import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user= User("chege","123","123")

    def test_init(self):

        self.assertEqual(self.new_user.username,"chege")
        self.assertEqual(self.new_user.password,"123")
        self.assertEqual(self.new_user.repeat_password,"123")

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):

        self.new_user.save_user()
        test_user = User("Test","321","321")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)






if __name__ == '__main__':
    unittest.main()    