
import json
import jsonpath
import requests

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send GET request and storing the response
response = requests.get(url)

# Display response content
print(response.content)
print("#################################")

# Display response header
print(response.headers)
print("#################################")

# Display response status code
print(response.status_code)

# Validate response status code. For that we use the 'assert' keyword
assert response.status_code == 200

# Fetch specific values from header
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch cookies from response
print(response.cookies)

# Fetch encoding from response
print(response.encoding)

# Fetch elapsed time from response
print(response.elapsed)

#########################################

# Parse response to Json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch pages value from json_response using Json Path and storing in pages variable
# We need to pass the parsed response 'json_response' and the 'jsonpath' we want to fetch
# The result is always stored in a list, so pages is a list
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 2

# Fetching firstname value.
# To get the first_name value from the data list, we use the syntax '.'
firstname = jsonpath.jsonpath(json_response, 'data[3].first_name')
print(firstname[0])