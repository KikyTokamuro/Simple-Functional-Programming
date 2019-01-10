#!/usr/bin/guile -s
!#

(define (incList l)
  (map 1+ l))

;; Функция, которая принимает другую функцию в качестве аргумента, и возвращает другую функцию как результат:
(define (changeList f l)
  (f l))

(write (changeList incList '(1 2 3))) ;; -> (2 3 4)
(newline)

;; Хранение функции в переменной
(define c changeList)

(write (c incList '(1 2 3))) ;; -> (2 3 4)
(newline)

;; Хранение функции в структурах данных предоставляемых языком:
;; В данном случае, хранение анонимной функции в хеш-таблице.
(define hashIncDec (make-hash-table))

(hash-set! hashIncDec 'inc (lambda (x) (+ x 1) ))
(hash-set! hashIncDec 'dec (lambda (x) (- x 1) ))

(write ((hash-ref hashIncDec 'inc) 5)) ;; -> 6
(newline)
(write ((hash-ref hashIncDec 'dec) 5)) ;; -> 4
(newline)
