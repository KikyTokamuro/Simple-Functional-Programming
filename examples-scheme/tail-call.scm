
#!/usr/bin/guile -s
!#

;; Функция вычисляющая факториал, используя хвостовую рекурсию:
;; Промежуточные вычисления храняться в `acc`.
(define (factorial-tail n)
  (define (factorial-acc n acc)
    (if (zero? n)
	acc
	(factorial-acc (- n 1) (* acc n))))
  (factorial-acc n 1))

(display (factorial-tail 5)) ;; -> 120
(newline)

(display (factorial-tail 10)) ;; -> 3628800
(newline)


;; Функция вычисляющая факториал, без хвостовой рекурсии:
(define (factorial n)
  (if (= n 1) 1 (* (factorial(- n 1)) n))) ;; Не считается хвостовым вызовом, так как еще есть операция умножения

(display (factorial 5)) ;; -> 120
(newline)

(display (factorial 10)) ;; -> 3628800
(newline)


