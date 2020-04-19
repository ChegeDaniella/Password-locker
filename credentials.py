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
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.username == username:
                return credentials 

    @classmethod
    def credential_exist(cls,username):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                    return True

        return False              