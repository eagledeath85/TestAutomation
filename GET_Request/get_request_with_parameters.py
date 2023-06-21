import requests


# Sending a get request with customized parameters
params = {"name": "Testing", "email": "testing.email@gmail.com", "phone_number": "+5548762355"}
response = requests.get("https://httpbin.org/get", params=params)
print(response.text)