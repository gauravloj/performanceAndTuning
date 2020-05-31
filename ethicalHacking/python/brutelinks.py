"""
1. run 'locate wordlist' to find the dictionary to use for brute force
2. Get the name attribute of username, password and submit button in the html file of target website

"""

import requests


page_url = "http://www.targetwebsit.com/"
dir_list = "directorylist.txt"   # this file contains possible directories a webpage can have

working_links = []

with open(dir_list, "r") as directories:
    for directory in directories:
        directory = directory.strip()
        full_url = page_url + directory

        # For subdomain, final url looks like :- http://subdomain.targetwebsite.com
        subdomain_url = page_url.replace("http://www","http://" + directory)
        print("Trying brute with " + full_url)

        response = None

        # Testing subdirectories
        try:
            response = requests.get(full_url)
        except requests.exceptions.ConnectionError:
            pass
        # If url is correct, then response will have some content
        if response:
            working_links.append(full_url)
            print("Foud working url: " + full_url)

        # testing subdomains
        try:
            response = requests.get(subdomain_url)
        except requests.exceptions.ConnectionError:
            pass
        # If url is correct, then response will have some content
        if response:
            working_links.append(subdomain_url)
            print("Foud working url: " + subdomain_url)
