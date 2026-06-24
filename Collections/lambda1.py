def add10_func(x):
    return x + 10

add10 = lambda x: x +10
print(add10(5))

#above two are the same


mult = lambda x,y : x+y
print(mult(2,7))

# lambda arguments: expression
points2D=[(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1]) #means: sort by the second element (y-coordinate)

print(points2D)
print(points2D_sorted)