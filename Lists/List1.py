my_list = ["Apple", "Banana", "Cherry"]
print(my_list)

# Create an empty list
my_list = list()
print(my_list)

# Create a list with mixed data types
my_list = ["Hello", 42, 3.14, True]
print(my_list)

item = my_list[0]
print("First item: " + item)

'''
item2 = my_list[1]
print("Second item: " + item2) # This will raise an error because we cannot concatenate a string and an integer

# To fix this, we can convert the integer to a string
item2 = my_list[1]
print("Second item: " + str(item2))

'''

item2 = my_list[1]
print("Second item: " + str(item2))

#or we can use string formatting
item3 = my_list[2]
print(f"Third item: {item3}")

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Indian Fig", "Jackfruit"]

for fruit in fruits:
    print(fruit)

if "Cherry" in fruits:
    print("Cherry is in the list ")
else:
    print("Cherry is not in the list ")

#print the length of the list
print(len(fruits))

#append a new item to the list
fruits.append("Kiwi")
print(fruits)

#insert a new item at a specific index
fruits.insert(2, "Lemon")
print(fruits)

#remove an item from the list
fruits.remove("Date")
print(fruits)

#remove an item by index
del fruits[3]
print(fruits)

#remove the last item from the list and return it
popped_item = fruits.pop()
print(f"Popped item: {popped_item}")
print(fruits)

#reverse the list
fruits.reverse()
print(fruits)

#sort the list
fruits.sort()
print(fruits)

#sort the list in reverse order
fruits.sort(reverse=True)
print(fruits)

#copy the list
fruits_copy = fruits.copy()
print(fruits_copy)


#count the number of occurrences of an item in the list
count = fruits.count("Apple")
print(f"Number of occurrences of Apple: {count}")

#find the index of an item in the list
index = fruits.index("Banana")
print(f"Index of Banana: {index}")

#extend the list with another list
more_fruits = ["Lemon", "Mango", "Nectarine"]
fruits.extend(more_fruits)
print(fruits)

#slice the list
sliced_fruits = fruits[2:5]
print(f"Sliced fruits: {sliced_fruits}")

#negative indexing
last_fruit = fruits[-1]
print(f"Last fruit: {last_fruit}")

#Enumerate the list
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#List comprehension to create a new list with the lengths of the fruit names( list length of each fruit name)
fruit_lengths = [len(fruit) for fruit in fruits]
print(f"Fruit lengths: {fruit_lengths}")

#Joining Lists into Strings
fruits_string = ", ".join(fruits)
print(f"Fruits string: {fruits_string}")

#Splitting Strings into Lists
fruits_list = fruits_string.split(", ")
print(f"Fruits list: {fruits_list}")

#Sorting with a Custom Key(by length of the fruit names)
fruits.sort(key=len)
print(f"Fruits sorted by length: {fruits}")

#Sorting with a Custom Key (case-insensitive)
fruits.sort(key=str.lower)

#clear the list
fruits.clear()
print(fruits)

#check if the list is empty
if not fruits:
    print("The list is empty")
else:
    print("The list is not empty")