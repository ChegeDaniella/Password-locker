#!/usr/bin/env python3.6
from user import User
import random, string

def generate_password(length):
    password=''

    for i in range(length):
        x = random.randint(0,95)
        password += string.printable[x]
    print(password)
    return password
    
generate_password(16)        

