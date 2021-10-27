package main

// binary search

import (
	"fmt"
	"math"
)

/**
 * @param x: a double
 * @return: the square root of x
 */
func sqrt(x float64) float64 {
	// write your code here
	if x == 0 || x == 1 {
		return x
	}
	l := float64(0)
	r := x
	gap := math.Pow10(-12)
	for l+gap < r {
		mid := (l + r) / 2
		fmt.Println(l, mid, r)
		if mid*mid == x {
			return mid
		} else if mid*mid < x {
			l = mid
		} else {
			r = mid
		}
	}

	if r*r <= x {
		return r
	}
	return l
}

func main() {
	a := float64(2)
	fmt.Println(sqrt(a))
}

