# Python Lists - Quick Notes

## What is a List?

A list is an ordered, mutable collection of items. Lists can store multiple values of different data types in a single variable.

```python
fruits = ["Apple", "Banana", "Cherry"]
mixed = ["Hello", 42, 3.14, True]
```

---

## Creating Lists

```python
fruits = ["Apple", "Banana", "Cherry"]
empty_list = []
empty_list = list()
```

---

## Accessing Elements

```python
fruits[0]      # First item
fruits[1]      # Second item
fruits[-1]     # Last item
fruits[-2]     # Second last item
```

---

## List Length

```python
len(fruits)
```

Returns the number of items in the list.

---

## Membership Testing

```python
if "Cherry" in fruits:
    print("Found")
```

---

## Looping Through a List

```python
for fruit in fruits:
    print(fruit)
```

With index:

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## Adding Elements

### Append

Adds an item to the end.

```python
fruits.append("Kiwi")
```

### Insert

Adds an item at a specific position.

```python
fruits.insert(2, "Lemon")
```

### Extend

Adds all items from another list.

```python
fruits.extend(["Mango", "Orange"])
```

---

## Removing Elements

### Remove by Value

```python
fruits.remove("Banana")
```

### Remove by Index

```python
del fruits[1]
```

### Pop

Removes and returns an item.

```python
item = fruits.pop()
```

---

## Sorting

Ascending:

```python
fruits.sort()
```

Descending:

```python
fruits.sort(reverse=True)
```

---

## Reversing

```python
fruits.reverse()
```

---

## Copying

```python
fruits_copy = fruits.copy()
```

---

## Counting Occurrences

```python
fruits.count("Apple")
```

---

## Finding Index

```python
fruits.index("Banana")
```

---

## Slicing

```python
fruits[1:4]
fruits[:3]
fruits[2:]
fruits[::-1]
```

---

## Useful Functions

```python
numbers = [10, 20, 30]

max(numbers)
min(numbers)
sum(numbers)
```

---

## Join a List into a String

```python
fruits = ["Apple", "Banana", "Cherry"]

result = ", ".join(fruits)
```

Output:

```text
Apple, Banana, Cherry
```

---

## Split a String into a List

```python
text = "Apple,Banana,Cherry"

fruits = text.split(",")
```

---

## List Comprehensions

Create lists in a compact way.

```python
squares = [x ** 2 for x in range(1, 6)]
```

Output:

```python
[1, 4, 9, 16, 25]
```

---

## Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])
```

Output:

```python
6
```

---

## Clear a List

```python
fruits.clear()
```

Removes all elements from the list.

---

## Key Points

* Lists are ordered.
* Lists are mutable (can be changed).
* Lists allow duplicate values.
* Lists can contain mixed data types.
* Indexing starts at 0.
* Negative indexing starts from the end.
* Lists are one of the most commonly used Python data structures.
