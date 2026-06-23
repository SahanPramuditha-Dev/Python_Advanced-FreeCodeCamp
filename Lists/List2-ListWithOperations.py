# Create a list with repeated values
my_list = [0] * 5
print("Repeated values:", my_list)

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Concatenation:", list1 + list2)

# Repeat a list
fruits = ["Apple", "Banana"]
print("Repeated list:", fruits * 3)

# Create a list from range
numbers = list(range(5))
print("Range:", numbers)

# Create a list from range with step
even_numbers = list(range(0, 11, 2))
print("Range with step:", even_numbers)

# Check if a list is empty
empty_list = []
if not empty_list:
    print("List is empty")

# Swap two elements
fruits = ["Apple", "Banana", "Cherry"]
fruits[0], fruits[2] = fruits[2], fruits[0]
print("Swapped:", fruits)

# Unpack a list
fruits = ["Apple", "Banana", "Cherry"]
a, b, c = fruits
print("Unpacked:", a, b, c)

# Maximum, minimum, and sum
numbers = [10, 20, 30, 40]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# Reverse using slicing
fruits = ["Apple", "Banana", "Cherry"]
print("Reversed:", fruits[::-1])

# Create a shallow copy
copy_fruits = fruits[:]
print("Copy:", copy_fruits)

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# Filter values with list comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Nested list item:", matrix[1][2])

# Join a list into a string
fruits = ["Apple", "Banana", "Cherry"]
joined = ", ".join(fruits)
print("Joined:", joined)

# Split a string into a list
text = "Apple,Banana,Cherry"
split_list = text.split(",")
print("Split:", split_list)

# Enumerate
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")