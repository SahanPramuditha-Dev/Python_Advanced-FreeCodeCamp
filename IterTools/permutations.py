from itertools import permutations

# Get input from user
text = input("Enter letters and numbers: ")

# Generate all possible variations
for p in permutations(text):
    print("".join(p))

print("---------------------------------------\nGenerate variations of all lengths\n---------------------------------------")

# Generate variations of all lengths
for length in range(1, len(text) + 1):
    for p in permutations(text, length):
        print("".join(p))