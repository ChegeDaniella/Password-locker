#log-in
import random, string
class Credentials:
    '''
    creates new instance of credentials
    '''
    credentials_list=[]

    def __init__(self,username,password,email):

        self.username = username
        self.email = email
        self.password = password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        
        return cls.credentials_list     

    # def generate_password(self):
    #     self.password=''

    #     for i in range(10):
    #         x = random.randint(0,95)
    #         password += string.printable[x]
    #         print(password)
    #     return password

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a account that matches that credentials.

        Args:
            username: username to search for
        Returns :
            Credentials of person that matches the usrname.
        '''

        for credentials in cls.credentials_list:
            if credentials.username == username:
                return credentials 

    @classmethod
    def credential_exist(cls,username):
        '''
        Method that checks if a username exists from the credentialslist.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if theusername exists
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                    return True

        return False              