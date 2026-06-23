# frozenset = immutable version of a set (cannot be changed after creation)

# creating a frozenset
A = frozenset([1, 2, 3, 4])
print(A)

# frozenset from string
B = frozenset("Hello World")
print(B)

# operations (allowed - they return new sets, do NOT modify original)

X = frozenset([1, 2, 3])
Y = frozenset([3, 4, 5])

print(X.union(Y))                 # combines elements
print(X.intersection(Y))          # common elements
print(X.difference(Y))            # elements in X not in Y
print(X.symmetric_difference(Y))  # non-common elements

# membership check
print(2 in X)
print(10 in X)

# length
print(len(X))

# ❌ NOT allowed (will cause error)
# X.add(5)
# X.remove(1)
# X.pop()
# X.update([5, 6])

# key idea:
# frozenset is hashable → can be used as dictionary keys or set elements

# example usage as dict key
data = {
    frozenset([1, 2]): "Group A",
    frozenset([3, 4]): "Group B"
}

print(data[frozenset([1, 2])])