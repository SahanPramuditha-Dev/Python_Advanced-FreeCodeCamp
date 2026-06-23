# creating a set (duplicates automatically removed)
myset = {1, 2, 3, 4}
print(myset)

# set from string (only unique characters kept)
greet = set("Good Morning")
print(greet)

# empty set
num_set = set()

# adding elements
num_set.add(1)
num_set.add(15)
num_set.add(8)
num_set.add(10)
num_set.add(26)

print(num_set)

# check membership before removing
print(8 in num_set)

# remove element (error if not found)
num_set.remove(8)

# discard element (no error if not found)
num_set.discard(26)

print(num_set)

# pop removes a random element
removed = num_set.pop()
print("popped:", removed)
print(num_set)

# clear all elements
num_set.clear()
print(num_set)

# set properties demo
letters = {"A", "D", "B", "Z", "S", "D", "W", "K"}
print(letters)

# length of set
print(len(letters))

# membership check
print("A" in letters)
print("X" in letters)

# iteration
for x in letters:
    print(x)

# convert list to set (removes duplicates)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# add multiple elements
letters.update(["M", "N", "O"])
print(letters)

# subset check
A = {1, 2}
B = {1, 2, 3, 4}
print(f"A is s Subset of B :",A.issubset(B))

# superset check
print(f"B is s Superset of A :",B.issuperset(A))

# disjoint check
C = {10, 20}
print(A.isdisjoint(C))

# copy set
copy_letters = letters.copy()
print(copy_letters)

# intersection update
A = {1, 2, 3, 4}
B = {3, 4, 5}
A.intersection_update(B)
print(A)

# difference update
A = {1, 2, 3, 4}
B = {3, 4}
A.difference_update(B)
print(A)

# symmetric difference update
A = {1, 2, 3}
B = {3, 4, 5}
A.symmetric_difference_update(B)
print(A)