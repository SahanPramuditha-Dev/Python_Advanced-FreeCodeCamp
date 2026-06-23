from collections import deque

# Initialize deque (double-ended queue)
# Supports fast operations at both ends
d = deque([1, 2, 3])

# Add elements
d.append(4)        # add to right end (stack/queue push)
d.appendleft(0)    # add to left end (fast front insertion)

# Remove elements
d.pop()            # remove from right end
d.popleft()        # remove from left end (fast queue dequeue)

# Rotate elements
d.rotate(1)        # shift right by 1
d.rotate(-1)       # shift left by 1

# Access elements (no removal)
front = d[0]       # leftmost element
back = d[-1]       # rightmost element

# Extend multiple elements
d.extend([5, 6])         # add to right
d.extendleft([-1, -2])   # add to left (note reverse order effect)

print(d)