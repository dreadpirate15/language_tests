// Solving Project Euler #9 in go

package main

import (
	"fmt"
)

func main () {
	for a := 1; a <= 1000; a++ {
		for b := a; b <= 1000; b++ {
			c := 1000 - (a + b)
			if (a*a)+(b*b) == (c*c) {
				fmt.Printf("Triplets - a: %d b: %d c: %d\n", a,  b,  c)
			}
		}
	}
}
