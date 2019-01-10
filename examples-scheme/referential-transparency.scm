#!/usr/bin/guile -s
!#

;; Ссылочная прозрачность
(define (square x)
	(* x x))
	
(write (= (+ (square 4) 2) (+ 16 2))) ;; -> #t
