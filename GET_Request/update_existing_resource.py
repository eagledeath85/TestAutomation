import requests
import json
import jsonpath


# API URL
# '2' can be configured as it is the id of the resource we want to update
url = 'https://reqres.in/api/users/2'

# Json file to send in PUT request
json_file = 'C:/Users/aallouche/Documents/Automation/update_user.json'

# 1. Read updated json from file
with open(json_file, 'r', encoding='utf-8', newline='') as file_to_send:
    json_input = file_to_send.read()

# 2. Parse into json format
request_json = json.loads(json_input)

# 3. Hit PUT method with request_json
put_response = requests.put(url, request_json)
assert put_response.status_code == 200

# 4. Parse response content to Json format
put_response_json = json.loads(put_response.text)
update_time = jsonpath.jsonpath(put_response_json, 'updatedAt')
print(update_time[0])

# 5. Validate response