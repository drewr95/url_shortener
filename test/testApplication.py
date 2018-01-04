import unittest
import requests

base_url = 'https://drew-urlshortener.herokuapp.com'

class TestHello(unittest.TestCase):

    def testHell0(self):
        response = requests.get(base_url)
        self.assertEqual({'Hello':'World!'}, response.json())
