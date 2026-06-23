from itertools import product

# Cartesian product = all possible combinations of elements

a = [1, 2]
b = [3, 4]

print(list(product(a, b)))
# [(1,3), (1,4), (2,3), (2,4)]

# Multiple iterables
print(list(product(a, b, [5, 6])))
# Combines all 3 lists

# Repeat mode (self-combination)
print(list(product(a, repeat=2)))
# [(1,1), (1,2), (2,1), (2,2)]

# Practical use: grid / coordinate generation
grid = list(product(range(2), range(2)))
print(grid)
# [(0,0), (0,1), (1,0), (1,1)]

# Key idea:
# product() replaces nested loops and generates all combinations efficiently