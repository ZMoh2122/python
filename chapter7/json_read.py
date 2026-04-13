import json

# Writing to a JSON file
data = {'name': 'Ahmed', 'age': 11, 'city': 'London'}
with open('output.json', mode='w') as file:
    json.dump(data, file, indent=4) # Indent for readability
