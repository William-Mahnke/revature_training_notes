# Basic zip — pairing two lists
names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 78]

zipped = zip(names, scores)
print(list(zipped)) # [('Alice', 95), ('Bob', 82), ('Charlie', 78)]
print(list(zipped)) # [] - recall that we can only iterate through an iterable once

# Iterating in parallel with zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 95
# Bob: 82
# Charlie: 78

# Zipping three iterables
roles = ["Admin", "User", "Guest"]
for name, score, role in zip(names, scores, roles):
    print(f"{name} ({role}): {score}")

# Building a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "London"]
profile = dict(zip(keys, values)) # dict()
print(profile)  # {'name': 'Alice', 'age': 30, 'city': 'London'}

# zip stops at the shortest iterable
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')] — 4 and 5 are dropped

# zip_longest — pads shorter iterables instead
from itertools import zip_longest
print(list(zip_longest(a, b, fillvalue="-")))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, '-'), (5, '-')]

# Unzipping — reversing a zipped sequence
pairs = zip(names, scores) # [("Alice", 95), ("Bob", 82), ("Charlie", 78)]
names_out, scores_out = zip(*pairs)
print(names_out)   # ('Alice', 'Bob', 'Charlie')
print(scores_out)  # (95, 82, 78)


