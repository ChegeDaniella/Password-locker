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

