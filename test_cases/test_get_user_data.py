import json
import jsonpath
import pytest
import requests


@pytest.mark.Smoke
def test_fetch_user_details():

    # API URL
    url = 'https://reqres.in/api/users?page=2'

    # Send GET request and storing the response
    response = requests.get(url)

    # Parse response to Json format
    json_response = json.loads(response.text)

    # Fetching firstname value.
    # To get the first_name value from the data list, we use the syntax '.'
    firstname = jsonpath.jsonpath(json_response, 'data[3].first_name')
    print(firstname[0])