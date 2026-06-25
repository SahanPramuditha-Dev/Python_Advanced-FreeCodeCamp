import json  # Import JSON module to work with JSON data formats

# Create a Python dictionary (key-value structured data)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# Convert Python dictionary to a JSON-formatted string
# indent=4 → makes output pretty and readable
# sort_keys=True → sorts dictionary keys alphabetically in output
personJSON = json.dumps(person, indent=4, sort_keys=True)

# Print the JSON string to console
print(personJSON)

with open("person.json","w") as file:
    json.dump(person, file, indent=4)









