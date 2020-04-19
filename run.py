#!/usr/bin/env python3.6
from user import User
import random, string
from credentials import Credentials

#function for creating new user
def create_user(Username,Password):

    new_user = User(Username,Password)
    return new_user   

#function for  creating new credentials
def create_credential(Username,Password,Email):

    new_credential  = Credentials(Username,Password,Email)  
    return new_credential   

#function for displaying the user accounts
def display_user():

    return User.display_user()

#function for displaying the user credentials
def display_credentials():    

    return Credentials.display_credentials() 

# Function to save user account
def save_users(user):

    user.save_user()   

# Function to save credentials
def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()   

def find_account(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_username(username)

def check_existing_credentials(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credential_exist(username)


def main():
        print("Hello welcome to creating a new account.What iis your name?")
        user_name = input()

        print(f"Hello{user_name}.Chose a path to take increating or opening your account")
        print('\n')

        while True:
            print("Use these shortcuts: oa - to open a new account, ea - input already exsisting accounts")
            path = input()

            if path == 'oa':
                
                print("Use this shortcuts : cu - create new account with your own password, dc - display") 

                short_code = input().lower()
                if short_code == 'cu':
                    print("Please enter your prefered username...")
                    Username = input() 

                    print("Please enter your preferred password...")
                    Password = input()

                    #create and save user 
                    save_users(create_user(Username,Password))  
                    print(f"New user account {Username}  has been created")   
                    print('\n')  

                #display contacts in user account
                elif short_code == 'dc':

                    if display_user():
                        print("Here is al list")
                        print('\n')

                        for User in display_user():
                            print(f"{User.Username} {User.Password}")

                    else:
                        print("No user accounts found") 

            elif path == 'ea':
                print("Use this shortcuts : cu - create new account, dc - display accounts, en - access your account") 

                short_code = input().lower()
                if short_code == 'cu':
                    print("Please enter your prefered username...")
                    Username = input() 

                    print("Please enter your email address...")
                    Email = input()

                    print("Use this short cuts to chose how to create a pass word.cp - create your own password,rp - a password to be generated ")   
                    password = input().lower()

                    if password == 'cp':
                        print("Create your own password.")
                        Password= input()

                    elif password == 'rp':
                        Passgenerate=''
                        for i in range(14):
                            x = random.randint(0,60)
                            Passgenerate += string.printable[x]
                            Password = Passgenerate

                    else: 
                        print("Please enter password.")

                    #create and save user 
                    save_credentials(create_credential(Username,Password,Email))  
                    print(f"New user account {Username} {Email} {Password}  has been created")   
                    print('\n') 

                elif short_code == 'dc':

                    if display_credentials():
                        print("Here is a list")
                        print('\n')

                        for Credentials in display_credentials():
                            print(f"{Credentials.username} {Credentials.Email} {Credentials.password}")

                    else:
                        print("No user accounts found") 
                elif short_code == 'en':

                    print("Please enter your username")
                    search_username = input()

                    if check_existing_credentials(search_username):
                        search_username = find_account(search_username)
                        print(f"{search_username.username} ")
                        print('-' * 20)

                        print(f"Password.......{search_username.password}")
                        print(f"Email address.......{search_username.email}")
                    else:
                        print("That contact does not exist")        
            else:
                print("Please chose a path you want to follow")             



if __name__ == '__main__':
            main()                   

           



    
      

