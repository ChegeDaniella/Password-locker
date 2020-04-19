#!/usr/bin/env python3.6
from user import User
import random, string
from credentials import Credentials

def create_user(Username,Password):
    new_user = User(Username,Password)
    return new_user

def display_user():
    return User.display_user() 

def save_users(user):

    User.save_user()

def main():
        print("Hello welcome to creating a new account.What iis your name?")
        user_name = input()

        print(f"Hello{user_name}.Chose a path to take increating or opening your account")
        print('\n')

        while True:
            print("Use these shortcuts: oc - to open a new account, dc - diplay accounts")
            path = input()

            # if path == 'oc':
                
            #     print("Use this shortcuts : cu - create new account with your own password, dc - display") 

            #     short_code = input().lower()
            # if short_code == 'cu':
            #     print("Please enter your prefered username...")
            #     Username = input() 

            #     print("Use this short cuts to chose how to create a pass word.cp - create your own password,rp - a password to be generated ")   
            #     password = input().lower()

            # if password == 'cp':
            #     print("Create your own password.")
            #     Password= input()
            # elif password == 'rp':
            #     password = random.randint(0,50)   
            #     Password=input() 
            # else: 
            #         print("Please enter password.")


            #         save_users(create_user(Username.password))#create and save user   
            #         print(f"New user account {Username} {password} has been created")   
            #         print('\n')  

            # elif short_code == 'dc':

            #     if display_user():
            #         print("Here is al list")
            #         print('\n')

            #         for User in display_user():
            #             print(f"{User.Username}")

            #     else:
            #         print("No user accounts found") 
if __name__ == '__main__':
            main()                    





    
      

