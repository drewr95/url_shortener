import requests
# import urlshortener.application

base_url = 'https://drew-urlshortener.herokuapp.com'

def test_hello():
    request = requests.get(base_url)
    assert 'Hello World!' == request.json()

    