# Обзор основных функций высшего порядка

## Map
Функция `map` принимает функцию, и какую либо последовательность (список, вектор, хеш и т.д). И применяет полученную функцию к полученной последовательности, и возвращает результат.

### Функция map в языке Python
```python
# Возведение каждого элемента списка в квадрат:
>>> list(map(lambda x: x**2, [1, 2, 3, 4]))
[1, 4, 9, 16]

# Перемножение чисел из двух списков:
>>> list(map(lambda x, y: x*y, [1, 2, 3, 4], [5, 6, 7, 8]))
[5, 12, 21, 32]

# Подсчет кол-ва букв в словах находящихся в списке:
>>> list(map(lambda x: len(x), ["Hello", "World", "Python"]))
[5, 5, 6]

# Использование словаря в функции Map:
>>> chars = {'a': 1, 'b': 2, 'c': 3}
>>> list(map(lambda x: x*chars[x], chars))
['a', 'bb', 'ccc']
```

### Функция map в языке Scheme (GNU Guile)
```scheme
scheme@(guile-user)> (map (lambda (x) (+ x 999)) '(1000 999 998 997 996))
$1 = (1999 1998 1997 1996 1995)
```

## Filter
Функция `filter` предназначена для фильтрации элементов последовательности. `filter` принимает в качестве аргументов функцию и последовательность, которую нужно отфильтровать. Функция в данном случае играет роль фильтра, который должен возвращать `True` либо `False`.

### Функция filter в языке Python
```python
# Генерация списка из четных чисел, от 0 до 100:
>>> list(filter(lambda x: x % 2 == 0, range(0, 101)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

# Фильтрация чисел, которые меньше/больше 10:
>>> list(filter(lambda x: x < 10, range(0, 21)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(filter(lambda x: x >= 10, range(0, 21)))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```

### Функция filter в языке Scheme (GNU Guile)
```scheme
scheme@(guile-user)> (filter even? '(1 2 3 4 5 6 7 8 9 10))
$1 = (2 4 6 8 10)

scheme@(guile-user)> (filter (lambda (x) (< x 5)) '(1 2 3 4 5 6 7 8 9 10))
$2 = (1 2 3 4)
```

## Reduce / Fold
Функция `reduce` принимает 2 аргумента: функцию и последовательность. `reduce` последовательно применяет функцию-аргумент к элементам последовательности, возвращает единичное значение. 

Большинство функций и рекурсивных алгоритмов может быть реализовано, с помощью функции `reduce` либо ее аналога `fold`. [Ссылка по этой теме.](http://www.cs.nott.ac.uk/~pszgmh/fold.pdf)

### Функция reduce в языке Python
В Python 2.x функция reduce является встроенной, а в Python 3 она находится в модуле functools.
```python
# Сумма чисел от 0 до 100:
>>> from functools import reduce
>>> reduce(lambda x, y: x + y, range(0, 101))
5050

>>> reduce(lambda x, y: 10 * x + y, [1,2,3,4,5,6,7,8,9])
123456789
```

### Функции fold и reduce в языке Scheme (GNU Guile)
[Более подробно про эти функции.](https://www.gnu.org/software/guile/manual/html_node/SRFI_002d1-Fold-and-Map.html)
```scheme
;; Сумма чисел от 0 до 100:
scheme@(guile-user)> (use-modules (srfi srfi-1))
scheme@(guile-user)> (fold + 0 (iota 101)) 
$1 = 5050
scheme@(guile-user) [17]> (reduce + 0 '(5 6 7))
$7 = 18
scheme@(guile-user)> (reduce + 0 '(5 6 7))
$2 = 18
```

## For Each 
Функция `for-each` - это нечистая функция высшего порядка, которая выполняет какой либо побочный эффект, для каждого элемента переданного списка. Так же, в отличии от функции `map`, функция `for-each` ничего не возвращает.

### Функция for-each в языке Scheme (GNU Guile)
```scheme
scheme@(guile-user)> (for-each (lambda (x y)
	    (display (string x y))
	    (newline))
	  (string->list "hello") (string->list "world"))
hw
eo
lr
ll
od
```

### Функция for_each в языке Python
Как таковой функции `for-each` в языке Python нет, но ее не сложно определить.
```python
def for_each(f, * xss):
	for xs in zip(* xss):
		f(*xs)

>>> for_each(print, range(0, 5))
0
1
2
3
4

>>> for_each(lambda x, y: print(x, y), range(0, 5), [*'abcde'])
0 a
1 b
2 c
3 d
4 e
```
