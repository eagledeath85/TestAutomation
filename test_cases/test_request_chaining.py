import requests
import json
import jsonpath


# Request chaining is the process in which we fetch data from a request and use this data to send another request
# The example below shows this process using test cases, but is not good practice as global keyword is used



def test_add_new_student():
    global student_id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    add_student_file = "/home/administrateur/Documents/API_Automation/add_student.json"
    with open(add_student_file, 'r', encoding='utf-8', newline='') as json_file:
        add_student_json = json.loads(json_file.read())
        post_response = requests.post(API_URL, add_student_json)
        print(post_response.text)
        student_id_list = jsonpath.jsonpath(post_response.json(), 'id')  # fetch the student id list from the response
        student_id = student_id_list[0]
        assert post_response.status_code == 201



def test_get_student_details():

    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(student_id)
    get_response = requests.get(API_URL)
    print(get_response.text)