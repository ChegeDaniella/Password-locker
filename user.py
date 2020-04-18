class User:
    """
    Class that generates new instances of user.
    """

    user_list=[]

    def __init__(self,username,password,repeat_password):

        self.username = username
        self.password = password
        self.repeat_password = repeat_password
   
    def save_user(self):

        User.user_list.append(self) 