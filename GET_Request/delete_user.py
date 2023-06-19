import requests


# API URL
url = 'https://reqres.in/api/users/2'

response = requests.delete(url)

# Fetch and validate response code. Successful deletion returns status code 204
response_status_code = response.status_code
print(response_status_code)
assert response_status_code == 204