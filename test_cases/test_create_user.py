import jsonpath
import pytest
import requests
import json


# API URL
url = 'https://reqres.in/api/users'

# Json file to send in POST request
json_file = 'C:/Users/aallouche/Documents/Automation/create_user.json'


@pytest.fixture
def start_exe(scope="module"):
    # 1. Read input json from file
    with open(json_file, 'r', encoding='utf-8', newline='') as file_to_send:
        json_input = file_to_send.read()

        # 2. Parse into json format
        yield json.loads(json_input)


@pytest.mark.Smoke
def test_create_user(start_exe):
    request_json = start_exe
    print(request_json)

    # 3. Hit POST method with request_json.
    # We pass first the url, then the request body
    # We store the response of the request and validate response status_code is 201
    post_response = requests.post(url, request_json)
    assert post_response.status_code == 201

    # 4. Parse response content to Json format
    post_response_json = json.loads(post_response.text)

    # Pick Id using Json path
    id = jsonpath.jsonpath(post_response_json, 'id')
    print(id[0])

    # 5. Validate response


@pytest.mark.Sanity
def test_create_other_user(start_exe):
    # 1. Read input json from file
    with open(json_file, 'r', encoding='utf-8', newline='') as file_to_send:
        json_input = file_to_send.read()

    # 2. Parse into json format
    request_json = json.loads(json_input)
    print(request_json)

    # 3. Hit POST method with request_json.
    # We pass first the url, then the request body
    # We store the response of the request
    post_response = requests.post(url, request_json)

    # 4. Parse response content to Json format
    post_response_json = json.loads(post_response.text)

    # Pick Id using Json path
    id = jsonpath.jsonpath(post_response_json, 'id')
    print(id[0])

    # 5. Validate response