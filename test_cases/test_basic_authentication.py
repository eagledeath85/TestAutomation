import requests
from requests.auth import HTTPBasicAuth


def test_login_with_basic_auth():
    # Sending requests to GitHub with basic auth user/password
    URL = 'https://api.github.com/user'
    USER = 'eagledeath85'
    PASSWORD = '8pBGbn9rIhFvUrJ'
    response = requests.get(URL, auth=HTTPBasicAuth(USER, PASSWORD))
    print(response.text)