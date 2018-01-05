import requests
import random
import string

short_characters = string.ascii_letters + string.digits


def create_short():
    return ''.join(random.choices(short_characters, k=5))


def getURL(url: str):
    """
    adds the proper http(s) prefix to the url if it doesn't already exist
    :param url: url string to be checked
    :return: proper url path
    """
    if "http" not in url:
        if "www" not in url:
            url = "http://www." + url
        else:
            url = "http://" + url

    return requests.get(url).url