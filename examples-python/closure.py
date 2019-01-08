#!/usr/bin/python3

# Замыкание - функция, которая запоминает среду в которой она была определена.
def sum(x):
    def sumXY(y):
        return x + y
    return sumXY

s = sum(10)
result = s(5)

print("s = sum(10)")
print("result = s(5)")
print("print(result) ->")

print(result) # -> 
