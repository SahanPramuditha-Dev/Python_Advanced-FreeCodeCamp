# Python List Slicing (Basic Examples)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig"]

# Basic slicing: start to end (end not included)
print(fruits[1:4])  
# ['Banana', 'Cherry', 'Date']

# From start to index
print(fruits[:3])  
# ['Apple', 'Banana', 'Cherry']

# From index to end
print(fruits[2:])  
# ['Cherry', 'Date', 'Elderberry', 'Fig']

# Copy of the list
print(fruits[:])  
# ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig']

# Step slicing
print(fruits[0:6:2])  
# ['Apple', 'Cherry', 'Elderberry']

# Reverse list
print(fruits[::-1])  
# ['Fig', 'Elderberry', 'Date', 'Cherry', 'Banana', 'Apple']

# Every second element
print(fruits[::2])  
# ['Apple', 'Cherry', 'Elderberry']

# Negative indexing with slicing
print(fruits[-4:-1])  
# ['Cherry', 'Date', 'Elderberry']

# Reverse a sliced portion
print(fruits[-4:][::-1])  
# ['Fig', 'Elderberry', 'Date', 'Cherry']