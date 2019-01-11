#!/usr/bin/guile -s
!#

;; Каррирование
(define (f x)
  (lambda (y) (+ (* x x) y)))

(write ((f 5) 10)) ;; -> 35
(newline)
