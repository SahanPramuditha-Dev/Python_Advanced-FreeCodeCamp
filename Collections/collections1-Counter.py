from collections import Counter

a = "aaaaaabbbbcc"
my_counter = Counter(a)
print(my_counter)

most_common_1 = my_counter.most_common(1)
print(most_common_1)

most_common_2 = my_counter.most_common(2)
print(most_common_2)

most_common_item = my_counter.most_common(1)[0]
print(most_common_item)

char, freq = most_common_item
print(char, freq)

b = "aaaaaabbbbccdddddd"
my_counter2 = Counter(b)
print(my_counter2)

most_common_b = my_counter2.most_common(1)[0]
print(most_common_b)

print(sum(my_counter2.values()))
print(len(my_counter2))

for k, v in my_counter2.items():
    print(k, v)

print(my_counter2.get('a', 0))
print(my_counter2.get('z', 0))

least_common = my_counter2.most_common()[:-3:-1]
print(least_common)

print(dict(my_counter2))

filtered = {k: v for k, v in my_counter2.items() if v >= 2}
print(filtered)