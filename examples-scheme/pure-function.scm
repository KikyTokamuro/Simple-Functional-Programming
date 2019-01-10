#!/usr/bin/guile -s
!#

;; Чистая функция, которая ничего не изменяет, и при одном и том же аргументе, всегда возвращает один и тот же результат:
(define (inc x) 
	(+ x 1))

(write (inc 10)) ;; -> 11
(newline)
(write (inc 10)) ;; -> 11
(newline)
(write (inc 10)) ;; -> 11
(newline)


;; Грязная функция, которая при одном и том же аргументе, возвращает разные результаты:
(define (rand-inc x)
	(+ (random 100) x))

(write (rand-inc 1))
(newline)
(write (rand-inc 1))
(newline)
(write (rand-inc 1))
(newline)