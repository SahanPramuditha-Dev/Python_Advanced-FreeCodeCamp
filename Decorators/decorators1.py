# This function is a decorator that adds extra behavior before and after another function
def start_end_decorator(func):

    # Wrapper function that will replace the original function
    def wrapper():
        # Code executed before the original function
        print("Start")

        # Call the original function passed into the decorator
        func()

        # Code executed after the original function
        print("End")

    # Return the wrapper function so it replaces the original function
    return wrapper


# Original function that simply prints a name
def print_name():
    print("Lucifer")


# Manually applying the decorator (function is being wrapped)
print_name = start_end_decorator(print_name)

# Calling the decorated function (actually calls wrapper)
print_name()