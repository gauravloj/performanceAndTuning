import requests


# keys for the headers are extracted from real response on the target website
myheaders = {
    "User-Agent" : "Oppo redmi",
    "Host" : "fakehost.com"  
}

response = requests.get("http://targetsite.com", headers=myheaders)
print(response.text)