#!/usr/bin/python3

# Функция с хвостовым вызовом:
def f(x):
    return tailCall(x * x) # Хвостовой вызов
	
# Функция вычисляющая факториал, используя хвостовую рекурсию:
# Промежуточные вычисления храняться в переменной `acc`.
def factorialTail(n, acc=1):
    if n == 0: return acc
    else: return factorialTail(n - 1, acc * n) # Хвостовой вызов

print("factorialTail(5) ->")
print(factorialTail(5)) # -> 120

print("factorialTail(10) ->")
print(factorialTail(10)) # -> 3628800


# Функция вычисляющая факториал, без хвостовой рекурсии:
def factorial(n):
    if n == 0: return 1
    else: return factorial(n-1) * n # Не считается хвостовым вызовом, так как еще есть операция умножения

print("\nfactorial(5) ->")
print(factorial(5)) # -> 120

print("factorial(10) ->")
print(factorial(10)) # -> 3628800
