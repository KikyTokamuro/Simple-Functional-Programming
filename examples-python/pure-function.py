#!/usr/bin/python3

# Чистая функция, которая ничего не изменяет, и при одном и том же аргументе, всегда возращает один и тот же результат:
def inc(x):
	return x + 1

print("inc(10) ->")
print(inc(10)) # -> 11

print("\ninc(10) ->")
print(inc(10)) # -> 11

print("\ninc(10) ->")
print(inc(10)) # -> 11


# Грязная функция, которая при одном и том же аргументе, возращает разные результаты:
# Грязные функции могут осуществлять ввод/вывод, так же они могут изменять состояние или глобальные переменные.
from random import randint

def randInc(x):
	return randint(0, 100) + x

print("\nrandInc(1) ->")
print(randInc(1))

print("\nrandInc(1) ->")
print(randInc(1)) 

print("\nrandInc(1) ->")
print(randInc(1)) 
