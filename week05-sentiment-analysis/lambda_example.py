from functools import reduce

def increase(n):
    return n + 1

def is_even(n):
    return n % 2 == 0

data = [23, 17, 12, 45, 11, 56, 78]

data = list(map(lambda x: increase(x), data))

print(data)

even = filter(lambda x: is_even(x), list(data))

print(list(even))

total = reduce(lambda x, y: x + y, data)
print(total)
