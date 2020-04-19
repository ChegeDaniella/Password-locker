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
    print("Hello welcome to creating a new account")
    user_name = input()

    print(f"Hello{user_name}.Chose a path to take increating yur passwords")
    print('\n')

    while True:
        print("Use this shortcuts : cu - create new account with your own password, dc - display") 

        short_code = input().lower()
        if short_code == 'cu':
            print("Please enter your prefered interface...")
            Username = input() 

            print("Use this short cuts to chose how to create a pass word.cp - create your own password ")  
            
            password = input().lower()
        if password == 'cp':
            print("Create your own password.")
        elif password == 'rp':
            password = random.randint(0,50)    
        else: 
                print("Please enter password.")

                save_users(create_user(Username,Password))#create and save user   
                print(f"New user account {Username} {password} has been created")     








            elif short_code == 'dc':

                if display_user():
                    print("Here is al list")
                    print('\n')

                    for User in display_user():
                        print(f"{User.Username}")

                else:
                    print("No user accounts found")        





    
      

