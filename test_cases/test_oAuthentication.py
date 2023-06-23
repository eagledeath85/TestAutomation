# oAuth method requires to send credentials to an application that will validate them
# and return an access token for this user.
# This access token will then be used for login by sending it as headers in the post request

# --------------------------------------------------------------------
# Step1: Send post request and generate authentication token
# Step2: Pick this token and store it into a variable
# Step3: Pass this token as header in further request

import json
import jsonpath
import requests


def test_oAuthentication():
    # We first need to grant access to the user in order to get response from api/StDetails
    # For that, we generate a token from the thetestingworldapi.com website
    token_url = "https://thetestingworldapi.com/Token"
    data_for_token_generation = {
        'grant_type': 'password',
        'username': 'admin',
        'password': 'adminpass'
        }
    response_token = requests.post(token_url, data_for_token_generation)
    #print(response_token.text)
    token = jsonpath.jsonpath(response_token.json(), 'access_token')    # Fetching the access_token from the response

    # Preparing the payload to send the API_URL
    auth = {
        'Authorization': 'Bearer ' + token[0]
    }

    # Sending post request with auth dictionary as headers
    API_URL = 'https://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL, headers=auth)
    print(response.text)