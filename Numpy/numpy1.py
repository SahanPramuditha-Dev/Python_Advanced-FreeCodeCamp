import numpy as np

# Create a 1D array (like a list but faster and more powerful)
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix)

# Check shape (rows, columns)
print(matrix.shape)

# Check data type
print(arr.dtype)

# Create array with zeros
zeros = np.zeros((2, 3))
print(zeros)

# Create array with ones
ones = np.ones((3, 3))
print(ones)

# Create a range of numbers
range_arr = np.arange(1, 10)
print(range_arr)

# Create numbers with equal spacing
linspace_arr = np.linspace(1, 10, 5)
print(linspace_arr)


a= np.random.randint(0,10)
print(a)

b= np.random.randint(0,10,3)
print(b)
