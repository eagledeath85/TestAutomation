import requests


# Sending a get request and saving the default headers to response variable
response = requests.get("https://httpbin.org/get")
print(response.text)

# We can add customized headers and pass them to the get request
headers_data = {"T1": "First_Header", "T2": "Second_Header"}
response = requests.get("https://httpbin.org/get", headers=headers_data)
print(response.text)