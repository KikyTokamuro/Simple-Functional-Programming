#!/usr/bin/guile -s
!#

;; Замыкание - функция, которая запоминает среду в которой она была определена.
(define (sum x)
  (lambda (y)
    (+ x y)))

(define sum-x-y (sum 10))

(write (sum-x-y 5)) ;; -> 15
