import json

# Parsing a JSON string
json_string = '{"name": "Zak", "age": 18, "city": "Minneapolis"}'
data = json.loads(json_string)
print(data["name"]) # {'name': 'Zak', 'age': 18, 'city': 'Minneapolis'}