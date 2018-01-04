import pytest
import requests
import urlshortener.application

base_url = 'https://drew-urlshortener.heroku.com'

def test_quick():
    assert 5 == 5