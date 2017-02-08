; applicative-order : all the arguments (定义，赋值...) are evaluated when th procedure is applied
;  先进行所有赋值，存储到环境，再进行运算
; normal-order : the evaluation of argument is procedured until the actual argument values ared needed
;  先进行运算，需要赋值变量时，再进行赋值操作 

 (define (p) (p))
 (define (test x y)
   (if (= x 0)
 	  0
       y))
 (test 0 (p))



;(define (try a b)
;(if (= a 0) 1 b))
;try(0 (/ 1 0))