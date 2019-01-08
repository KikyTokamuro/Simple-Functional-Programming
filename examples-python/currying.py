#!/usr/bin/python3

# Каррирование
def f(x):
    return lambda y: x * x + y

print("f(5)(10) ->")
print(f(5)(10)) # -> 35
