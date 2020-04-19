#Sign-up
class User:
    """
    Class that generates new instances of user.
    """

    user_list=[]

    def __init__(self,username,password):

        self.username = username
        self.password = password
        
   
    def save_user(self):

        User.user_list.append(self) 

    @classmethod
    def display_user(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list    

