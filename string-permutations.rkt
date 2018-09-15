#lang typed/racket
(require typed/rackunit)

; All string permutations (alphabet = {A, B, C}) of a given length.
(: string-permutations
   (Exact-Nonnegative-Integer (Listof String) -> (Listof String)))
(define (string-permutations str-size alphabet)
  (cond
    [(= 0 str-size) empty]
    [(= 1 str-size) alphabet]
    [else
     ((inst map String String) 
      (lambda ([permutation : String])
        ((inst map String String)
         (lambda ([letter : String])
           (string-append letter permutation)) alphabet))
      (string-permutations (- str-size 1) alphabet))]
    #;[else
     (flatten (map (lambda ([permutation : String])
                     (map (lambda ([letter : String])
                            (string-append letter permutation)) alphabet))
                   (string-permutations (- str-size 1) alphabet)))]))

(string-permutations 0 (list "A" "B"  "C"))
(string-permutations 1 (list "A" "B"  "C"))
(string-permutations 2 (list "A" "B"  "C"))
(string-permutations 3 (list "A" "B"  "C"))