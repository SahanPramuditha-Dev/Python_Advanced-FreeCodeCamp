# Import namedtuple factory from collections module
from collections import namedtuple

# Create a new lightweight class called "Point"
# This defines a structure with two fields: x and y
coordinate = namedtuple("Point", "x,y")

# Create an instance of the coordinate (Point) structure
# Values are assigned to x and y respectively
pt = coordinate(1, -4)

# Print the named tuple object
# Output will include field names for clarity
print(pt)


print(pt.x,pt.y)