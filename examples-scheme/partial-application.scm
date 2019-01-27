#!/usr/bin/guile -s
!#

(define (partial fun . args)
  (lambda x (apply fun (append args x))))


;; Обычная функция принимающая 3 аргумента:
(define (f x y z)
  (* (+ x y z) 100))

(display (f 2 3 4)) ;; -> 900
(newline)


;; Частичное применение этой же функции:
(define (funcYZ y z)
  ((partial f 2) y z)) ;; x = 2

(display (funcYZ 3 4)) ;; -> 900
(newline)

(display ((partial f 2) 3 4)) ;; 900
(newline)


