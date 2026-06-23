# basic string
my_string = "Hello World !"
print(my_string)

# string with apostrophe
my_string1 = "I'm a Programmer."
print(my_string1)

# multiline string
my_string2 = """This is
My World."""
print(my_string2)

# accessing characters using index
name = "Sahan Pramuditha"

# first character
print(name[0])

# last character
print(name[-1])

# second character
print(name[1])

# third character from end
print(name[-3])

# string slicing
my_string4 = "I am a Devil of My Word"

# characters from index 7 to 11
print(my_string4[7:12])

# first 5 characters
print(my_string4[:5])

# from index 10 to end
print(my_string4[10:])

# entire string
print(my_string4[:])

# reverse string
print(my_string4[::-1])

# Strings are immutable
'''
my_string4[0] = "H"
'''

# string concatenation
greeting = "Good Morning"
name = "Lucifer"

sentence = greeting + " " + name
print(sentence)

# string repetition
print("Hi " * 3)

# loop through characters
for char in sentence:
    print(char)

# membership operator
if "e" in name:
    print("'e' exists in name")

if "z" not in name:
    print("'z' does not exist in name")

# string length
print(len(name))

# remove spaces
text = "      Hello Lucifer      "
print(text)

text = text.strip()
print(text)

# uppercase
print(text.upper())

# lowercase
print(text.lower())

# title case
print(text.title())

# capitalize first letter
print(text.capitalize())

# startswith
print(text.startswith("Hello"))

# endswith
print(text.endswith("Lucifer"))

# find substring
print(text.find("o"))

# returns -1 if not found
print(text.find("xyz"))

# count occurrences
print(text.count("l"))

# replace text
print(text.replace("Lucifer", "Samael"))

# split using spaces
intro = "Hello My Name is Lucifer Morningstar"

words = intro.split(" ")
print(words)

# split using comma
fruits = "apple,banana,cherry,orange"

fruit_list = fruits.split(",")
print(fruit_list)

# join list into string
words_list = ["Python", "is", "fun", "to", "learn"]

sentence = " ".join(words_list)
print(sentence)

# repeat list items
multi = ["a"] * 6
print(multi)

# checking data types
print(type(my_string))
print(type(sentence))

# string formatting using f-string
name = "Lucifer"
age = 10000

print(f"My name is {name} and I am {age} years old.")

# formatting with format()
print("My name is {}.".format(name))

# formatting multiple values
print("Name: {}, Age: {}".format(name, age))

# index method
print(text.index("H"))

# checking alphabetic characters
print("Python".isalpha())

# checking numeric characters
print("12345".isdigit())

# checking alphanumeric characters
print("Python123".isalnum())

# checking lowercase
print("hello".islower())

# checking uppercase
print("HELLO".isupper())

# swap uppercase and lowercase
print("Hello Lucifer".swapcase())

# center a string
print("Python".center(20))

# left justify
print("Python".ljust(20))

# right justify
print("Python".rjust(20))

# remove specific characters from beginning and end
text2 = "###Python###"
print(text2.strip("#"))

# escape characters
print("Hello\nWorld")
print("Hello\tWorld")

# raw string
print(r"C:\Users\Sahan\Documents")

# converting string to list
word = "Python"
letters = list(word)
print(letters)

# checking string comparison
print("apple" == "apple")
print("apple" == "Apple")

# ASCII value of a character
print(ord("A"))

# character from ASCII value
print(chr(65))