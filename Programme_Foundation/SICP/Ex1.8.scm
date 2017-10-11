(define (cube-root x)
	 (cube-root-iter 1.0 x ))
  


(define (cube-root-iter guess x )
  ( if (goodenough guess x)
     guess
	 (cube-root-iter (improve guess x)
	              x)))

 
(define (goodenough guess x)
	(< (abs(- (cube guess) x))
	   0.01))
    
     
(define (improve guess x )
	(/ (+ (/ x (square guess )) (* 2 guess)) 3))

(define (cube x)
(* x x x))


(cube-root 8)
