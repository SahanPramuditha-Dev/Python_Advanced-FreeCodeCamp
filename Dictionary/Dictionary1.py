my_dictionary = {
    "name": "Lucifer Morningstar",
    "age": 1000,
    "location": "Hell",
    "partner": "Chloe Decker"
}

print(my_dictionary)

my_dictionary2 = dict(name="Lucifer Morningstar", age=1000, location="Hell", partner="Chloe Decker")
print(my_dictionary2)

value = my_dictionary["name"]
print(f"Name: {value}")

my_dictionary["age"] = 2000 # Update the age
print(my_dictionary)

my_dictionary["occupation"] = "CEO of Lux" # Add a new key-value pair
print(my_dictionary)

if "name" in my_dictionary:
    print(f"Yes name is here. Name is {my_dictionary['name']}.")

'''
keytoSearch = input("Enter Your Key: ")

try:
    print(my_dictionary[keytoSearch])
except:
    print(f"Error no key as {keytoSearch}")

'''

for key in my_dictionary.keys():
    print(key)

for value in my_dictionary.values():
    print(value)


for key,value in my_dictionary.items():
    print(key,value)

#update
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)
