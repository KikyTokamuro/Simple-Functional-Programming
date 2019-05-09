# Комбинаторы

Комбинатор - это набор примитивных функций, операторов и функций высокого порядка, которые можно комбинировать для создания более сложных функций.
Комбинатор - это единица, которой оперирует [комбинаторная логика](https://ru.wikipedia.org/wiki/Комбинаторная_логика). Так же комбинаторы используются в [комбинаторной парадигме программирования](https://ru.wikipedia.org/wiki/Комбинаторное_программирование), которая является особой разновидностью функционального программирования.

Комбинаторы могут быть использованы для построения EDSL ([встраиваемый предметно-специфичный язык](https://ru.wikipedia.org/wiki/Предметно-ориентированный_язык)).

Блоки для построения комбинаторов:
- Обычные примитивные функции
- Функции высшего порядка
- Алгебраические типы данных
- Бинарные операторы

Если брать за пример язык программирования Haskell, то в нем присутствуют такие комбинаторы:
- Функции комбинаторов: id, (.), const, ($), flip, (&), on, fix, join, ap
- Функции обработки списков: map, filter, zip, fold
- Монады-комбинаторы: Haskell’s Maybe monad, Either Monad, IO Monad, ...
- Parsec - это библиотека для парсинга комбинаторов

### Реализация основных комбинаторов на языке Scheme (Chicken):
[Репозиторий с моим исходником](https://github.com/KikyTokamuro/chicken-combinators)
```scheme
;; Identity
(define (I x) x)

;; Constant
(define (K x)
  (lambda (y) x))

;; Apply
(define (A f)
  (lambda (x) (f x)))

;; Trush
(define (T x)
  (lambda (f) (f x)))

;; Duplication
(define (W f)
  (lambda (x) (f x x)))

;; Flip
(define (C f)
  (lambda (y)
    (lambda (x) (f x y))))

;; Compose
(define (B f)
  (lambda (g)
    (lambda (x) (f (g x)))))

;; Substitution
(define (S f)
  (lambda (g)
    (lambda (x) (f x (g x)))))

;; Psi
(define (P f)
  (lambda (g)
    (lambda (x)
      (lambda (y)
(f (g x) (g y))))))
```

[Комбинаторы - это просто!](https://ru.wikibooks.org/wiki/Комбинаторы_—_это_просто!)

[Common combinators in JavaScript](https://gist.github.com/Avaq/1f0636ec5c8d6aed2e45)

[Комбинаторная логика в программировании](http://labs.rulezz.ru/files/118/cl.pdf)
