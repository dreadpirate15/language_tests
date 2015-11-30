(defun triplets ()
  (print "Starting up")
  (loop
   for a from 1 to 1000
   do
   (loop
    for b from a to 1000
    if (equal
    	(+ (* a a) (* b b))
    	(*
    	 (- 1000 (+ a b))
	 (- 1000 (+ a b))
    	 )
    	)
    do (format t "Triplet: ~a" (list a b (- 1000 (+ a b))))
    )
   )
)

(triplets)
