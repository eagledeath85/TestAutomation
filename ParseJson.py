import json

odics = '{"Key1": "Value1", "Key2": "Value2"}'

# loads() will parse the string odics into json format
json_result = json.loads(odics)


print(json_result)
print(json_result["Key1"])