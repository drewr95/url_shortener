import requests
import urlshortener.url

base_url = 'https://drew-urlshortener.herokuapp.com'

def testHello():
    request = requests.get(base_url)
    assert 'Hello World!' == request.json()

def testGetURL():
    url = 'google.com'
    assert 'http://www.google.com/' == urlshortener.url.getURL(url=url)

def testAdd():
    url = base_url + "/add"
    headers = {'long':'google.com'}
    print(requests.get(url, headers=headers).json())
    assert requests.get(url, headers=headers).json() is not None



