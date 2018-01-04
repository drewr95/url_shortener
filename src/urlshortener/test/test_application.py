import requests
from urlshortener import application

base_url = 'https://drew-urlshortener.herokuapp.com'

def testHello():
    request = requests.get(base_url)
    assert 'Hello World!' == request.json()

def testGetURL():
    url = 'google.com'
    assert 'http://www.google.com/' == application.getURL(url=url)



