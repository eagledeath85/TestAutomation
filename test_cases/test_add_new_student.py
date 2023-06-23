import json
import jsonpath
import requests



def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    student_details_json = "C:/Users/aallouche/Documents/Automation/studentDetails.json"
    with open(student_details_json, 'r', encoding='utf-8', newline='') as json_file:
        json_request = json.loads(json_file.read())
        response_post = requests.post(API_URL, json_request)
    print(response_post.text)


def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7606263"
    response_get = requests.get(API_URL)
    json_response_get = json.loads(response_get.text)
    # We could also write the following: json_response_get = response_get.json()
    student_id = jsonpath.jsonpath(json_response_get, 'data.id')
    assert student_id[0] == 7606263


def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7606263"
    student_details_json = "C:/Users/aallouche/Documents/Automation/update_studentDetails.json"
    with open(student_details_json, 'r', encoding='utf-8', newline='') as json_file:
        json_request = json.loads(json_file.read())
        response_put = requests.put(API_URL, json_request)
        print(response_put.text)


def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7606263"
    response_delete = requests.delete(API_URL)
