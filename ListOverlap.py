# Program 3

# Take two lists and write a program that returns a list that only contains the elements that are common (without duplicates)
# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python

import random

a = random.sample(range(30), 5)
b = random.sample(range(10), 5)
c = []

for elem in a:
    if elem in b:
        c.append(elem)

print(a, b, c)

final = list(set(c))

print(final)

# Extra 2
print(set(a) & set(b))

