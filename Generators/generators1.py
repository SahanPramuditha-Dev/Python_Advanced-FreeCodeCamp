# Generators are functions that use the yield keyword.
# Unlike return, yield does not end the function.
# It pauses the function and remembers its current state.
# When the next value is requested, the function continues
# from where it previously stopped.


# Example 1: Simple Generator

def counter(limit):

    # Start counting from 1
    i = 1

    # Keep running while i is less than or equal to limit
    while i <= limit:

        # Give the current value to the caller
        # and pause the function here
        yield i

        # When the generator resumes,
        # execution continues from this line
        i += 1


# Create a generator object
numbers = counter(5)

# The for loop automatically calls next()
# until the generator finishes
for num in numbers:
    print(num)


print()


# Example 2: Understanding next()

def simple_gen():

    print("Step 1")
    yield 10

    print("Step 2")
    yield 20

    print("Step 3")
    yield 30


# Create generator object
g = simple_gen()

# Starts function execution
# Prints "Step 1"
# Returns 10
print(next(g))

# Continues after first yield
# Prints "Step 2"
# Returns 20
print(next(g))

# Continues after second yield
# Prints "Step 3"
# Returns 30
print(next(g))


print()


# Example 3: Generate Square Numbers

def squares(limit):

    i = 1

    while i <= limit:

        # Calculate square of current number
        square = i * i

        # Return square and pause
        yield square

        # Continue here next time
        i += 1


for num in squares(5):
    print(num)


print()


# Example 4: Generate Even Numbers

def even_numbers(limit):

    i = 1

    while i <= limit:

        # Check if number is divisible by 2
        if i % 2 == 0:

            # Return only even numbers
            yield i

        i += 1


for num in even_numbers(10):
    print(num)


print()


# Example 5: Fibonacci Generator

def fibonacci():

    # First two Fibonacci numbers
    a = 0
    b = 1

    while True:

        # Return current value
        yield a

        # Calculate next pair of numbers
        a, b = b, a + b


# Create generator object
fib = fibonacci()

# Request first 10 Fibonacci numbers
for i in range(10):
    print(next(fib))


print()


# What happens internally?
#
# fib = fibonacci()
#
# next(fib) -> returns 0
# next(fib) -> returns 1
# next(fib) -> returns 1
# next(fib) -> returns 2
# next(fib) -> returns 3
#
# Each call resumes from the previous yield.


# Key Difference
#
# return:
#
# def test():
#     return 1
#
# Function ends immediately.
#
#
# yield:
#
# def test():
#     yield 1
#     yield 2
#     yield 3
#
# Function pauses after each yield
# and continues when asked for the next value.