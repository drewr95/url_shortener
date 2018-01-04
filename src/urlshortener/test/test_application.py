import requests

base_url = 'https://drew-urlshortener.herokuapp.com'

def testHello():
    request = requests.get(base_url)
    assert 'Hello World!' == request.json()

# def testGetURL():




