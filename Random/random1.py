import random

# random() generates a float between 0 and 1
a = random.random()
print(a)

# uniform(a, b) generates a float between a and b
b = random.uniform(1, 10)
print(b)

# randint(a, b) generates an integer between a and b (both included)
c = random.randint(1, 10)
print(c)

# randrange(a, b) generates an integer from a to b-1 (b is excluded)
d = random.randrange(1, 10)
print(d)

# normalvariate(mean, stddev) generates values based on normal distribution
e = random.normalvariate(0, 1)
print(e)

# Create a list of characters from A to H
mylist = list("ABCDEFGH")
print(mylist)

# choice() selects one random element from the list
f = random.choice(mylist)
print(f)

# sample() selects k unique elements without repetition
g = random.sample(mylist, 3)
print(g)

# choices() selects k elements and allows repetition
h = random.choices(mylist, k=3)
print(h)

# shuffle() rearranges the list in place and returns None
random.shuffle(mylist)
print(mylist)

# seed() sets the starting point for random number generation
# same seed produces the same sequence of results every time
random.seed(1)

print(random.random())
print(random.randint(1, 10))

# resetting the seed restarts the same sequence again
random.seed(1)

print(random.random())
print(random.randint(1, 10))


