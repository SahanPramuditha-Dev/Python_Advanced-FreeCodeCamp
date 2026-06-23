# Set of even numbers
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18}

# Set of odd numbers
odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

# Set of prime numbers
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}

# UNION: combines both sets, removes duplicates
u = odd_numbers.union(even_numbers)
print(u)
# Output (order may vary):
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

# INTERSECTION: common elements between even numbers and prime numbers
i = even_numbers.intersection(prime_numbers)
print(i)
# Output:
# {2}

# Another example sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# DIFFERENCE: elements in setA that are NOT in setB
diff = setA.difference(setB)
print(diff)
# Output:
# {4, 5, 6, 7, 8, 9}

# SYMMETRIC DIFFERENCE: elements in either setA or setB but NOT in both
diff1 = setB.symmetric_difference(setA)
print(diff1)

# Output:
# {4, 5, 6, 7, 8, 9, 10, 11, 12}

# disjoint check (no common elements)
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
# True → no elements are shared between A and B


# copy operation (creates a separate set)
set1 = {10, 20, 30}
set2 = set1.copy()

print(set2)
# {10, 20, 30}


# intersection update (keeps only common elements, modifies original set)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)
# {3, 4}


# difference update (removes elements found in other set)
A = {1, 2, 3, 4}
B = {3, 4}

A.difference_update(B)

print(A)
# {1, 2}


# symmetric difference update (keeps only non-common elements)
A = {1, 2, 3}
B = {3, 4, 5}

A.symmetric_difference_update(B)

print(A)
# {1, 2, 4, 5}