import requests
import json
import jsonpath
from configparser import ConfigParser



config = ConfigParser()
config.read("/home/administrateur/PycharmProjects/TestAutomation/InputFiles/Config.cfg")
base_url = config.get('APIAutomation', 'base_url')


def test_add_multiple_students():
    api_url = f'{base_url}/api/studentsDetails'
    add_student_file = "/home/administrateur/Documents/API_Automation/add_student.json"
    with open(add_student_file, 'r', encoding='utf-8', newline='') as json_file:
        add_student_json = json.loads(json_file.read())
        post_response = requests.post(api_url, add_student_json)
    assert post_response.status_code == 201