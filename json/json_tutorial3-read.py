import json  # Handles JSON parsing (JSON → Python)

# Open the JSON file in read mode
with open("person.json", "r") as file:
    
    # Convert JSON file content → Python dictionary
    person = json.load(file)

# Output the reconstructed Python object
print(person)
