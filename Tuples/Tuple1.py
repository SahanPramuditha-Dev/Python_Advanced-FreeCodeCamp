#tuple is an ordered, immutable collection of items. Tuples are defined using parentheses () and can contain elements of different data types.

my_tuple = ("Lucifer", "Morningstar", 1000, True)
print(my_tuple)

my_tuple2 = "Hello", "World", 42, False # Parentheses are optional, but it's good practice to use them for clarity
print(my_tuple2)

my_tuple3 = ("SingleElement",) # Note the comma, it's necessary for single-element tuples
print(my_tuple3)

my_tuple4 = tuple(["Apple", "Banana", "Cherry"]) # Creating a tuple from a list
print(my_tuple4)

item = my_tuple[0]
print("First item: " + item)

#print each item in the tuple
for item in my_tuple:
    print(item)

#check if an item is in the tuple
if "Morningstar" in my_tuple:
    print("Morningstar is in the tuple")

letters = ("A", "B", "C", "D", "E","A","A","A","E","D","C","B","A")

#count how many times "A" appears in the tuple
print("Count of A:", letters.count("A"))

#find the index of the first occurrence of "A"
print("Index of first A:", letters.index("A"))

#find the index of the last occurrence of "A"
print("Index of last A:", len(letters) - 1 - letters[::-1].index("A"))

details = "Lucifer Morningstar","1000","Hell","Chloe Decker"

Name, Age, Location, Partner = details

print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"Location: {Location}")
print(f"Partner: {Partner}")

numbers = (1, 2, 3, 4, 5)
i1, i2, i3, i4, i5 = numbers
print(f"i1: {i1}, i2: {i2}, i3: {i3}, i4: {i4}, i5: {i5}")

numbers2= (10, 20, 30, 40, 50)
i1, *rest = numbers2
print(f"i1: {i1}, rest: {rest}")

numbers3 = (100, 200, 300, 400, 500)
i1, *middle, i5 = numbers3
print(f"i1: {i1}, middle: {middle}, i5: {i5}")