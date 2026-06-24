try:
    a = 5 / 0 
except :
    print("An Error Has Occured")


try:
    b = 100 / 0
except Exception as e:
    print(e)

try:
    c = 100 / 0
except ZeroDivisionError as e:
    print(e)


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


try:
    a=5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e) 