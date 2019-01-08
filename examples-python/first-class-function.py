#!/usr/bin/python3

# Функция которая принимает другую функцию в качестве аргумента, и возращает другую функцию как результат:
def inc(l):
    return [x + 1 for x in l]

def changeList(f, l):
    return f(l)

# changeList(f, l) = f(l)
print("changeList(inc, [1, 2, 3]) ->")
print(changeList(inc, [1, 2, 3])) # -> [2, 3, 4]


# Хранение функции в переменной
c = changeList
print("\nc = changeList\nc(inc, [2, 3]) ->")
print(c(inc, [2, 3])) # -> [3, 4]


# Хранение функций в структурах данных предоставляемых языком:
hashIncDec = {
    'inc': lambda x: x + 1,
    'dec': lambda x: x - 1
}

print("\nhashIncDec['inc'](10) ->")
print(hashIncDec['inc'](10)) # -> 11

print("\nhashIncDec['dec'](10) ->")
print(hashIncDec['dec'](10)) # -> 9



