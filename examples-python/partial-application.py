#!/usr/bin/python3

from functools import partial

# Обычная функция принимающая 3 аргумента:
def f(x, y, z):
    return (x + y + z) * 100

print("f(2, 3, 4) ->")
print(f(2, 3, 4)) # -> 900


# Частичное применение этой же функции:
funcYZ = partial(f, 2) # x = 2

print("\nfuncYZ(3, 4) ->")
print(funcYZ(3, 4)) # -> 900

print("\npartial(f, 2)(3, 4) ->")
print(partial(f, 2)(3, 4)) # -> 900
