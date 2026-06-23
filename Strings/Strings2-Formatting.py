# String formatting using %s (string)
var = "Tom"
my_string = "The variable is %s" % var
print(my_string)

# %d converts the value to an integer
var1 = 3.14752556
my_string1 = "The variable is %d" % var1
print(my_string1)

# %f displays a float (6 decimal places by default)
var2 = 3.14752556
my_string2 = "The variable is %f" % var2
print(my_string2)

# Using the format() method
var3 = 3.14752556
my_string3 = "The variable is {}".format(var3)
print(my_string3)

# Display only 2 decimal places
var4 = 3.14752556
my_string4 = "The variable is {:.2f}".format(var4)
print(my_string4)

# Multiple values with format()
name = "Sahan"
age = 20
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# Using index positions
message2 = "Name: {0}, Age: {1}".format(name, age)
print(message2)

# Reusing the same value
message3 = "{0} loves Python. {0} practices every day.".format(name)
print(message3)

# Named placeholders
message4 = "Name: {name}, Age: {age}".format(
    name="Sahan",
    age=20
)
print(message4)

# Number formatting
number = 1234567

# Add commas to large numbers
print("{:,}".format(number))

# Display 3 decimal places
pi = 3.14159265359
print("{:.3f}".format(pi))

# Convert decimal to percentage
score = 0.89
print("{:.1%}".format(score))

# Order summary example
item_name = "Wireless Headphones"
quantity = 3
price_per_unit = 49.99

order_summary = "You ordered {} x {} for a total of ${:.2f}.".format(
    quantity,
    item_name,
    quantity * price_per_unit
)

print(order_summary)

# Student report example
student_name = "Sahan"
marks = 87.456

report = "Student: {} | Marks: {:.2f}".format(
    student_name,
    marks
)

print(report)

# Invoice example
product = "Laptop"
qty = 2
price = 850.75

invoice = """
Product : {}
Quantity: {}
Price   : ${:.2f}
Total   : ${:.2f}
""".format(
    product,
    qty,
    price,
    qty * price
)

print(invoice)

# f-strings (recommended in modern Python)
name = "Sahan"
age = 20

print(f"My name is {name} and I am {age} years old.")

price = 49.99
quantity = 3

print(f"Total Price = ${price * quantity:.2f}")

# Expressions inside f-strings
print(f"10 + 20 = {10 + 20}")

# Formatting decimals
pi = 3.14159265359
print(f"Pi = {pi:.4f}")

# %s     -> String
# Used to insert a string into another string
name = "Sahan"
print("Hello %s" % name)

# %d     -> Integer
# Converts and prints only integer part
value = 3.99
print("Integer value: %d" % value)

# %f     -> Float
# Default prints 6 decimal places
pi = 3.14159265359
print("Pi value: %f" % pi)

# %.2f   -> Float with 2 decimal places
price = 49.999
print("Price: %.2f" % price)


# {}     -> format() placeholder
name = "Sahan"
print("My name is {}".format(name))

# {:.2f} -> 2 decimal places
value = 3.14159
print("Value: {:.2f}".format(value))

# {:,}   -> Comma separator (useful for large numbers)
number = 10000000
print("Number: {:,}".format(number))

# {:<10} -> Left align (padding with spaces)
text = "Python"
print("Left: '{:<10}'".format(text))

# {:>10} -> Right align
print("Right: '{:>10}'".format(text))

# {:^10} -> Center align
print("Center: '{:^10}'".format(text))


# f"{x}" -> f-string (modern formatting)
name = "Sahan"
age = 20
print(f"My name is {name} and I am {age} years old")

# f-string with expressions
a = 10
b = 20
print(f"Sum: {a + b}")

# f-string with formatting
pi = 3.14159265359
print(f"Pi rounded: {pi:.2f}")



# ==========================================
# Common Formatting Symbols
# ==========================================
#
# %s     -> String
# %d     -> Integer
# %f     -> Float
# %.2f   -> Float with 2 decimal places
#
# {}     -> format() placeholder
# {:.2f} -> 2 decimal places
# {:,}   -> Comma separator
# {:<10} -> Left align
# {:>10} -> Right align
# {:^10} -> Center align
#
# f"{x}" -> f-string
#
# ==========================================