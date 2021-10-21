package main

// stack
// time O(n)

import (
	"fmt"
)

/**
 * @param height: A list of integer
 * @return: The area of largest rectangle in the histogram
 */
func largestRectangleArea(height []int) int {
	// write your code here
	n := len(height)
	if n == 0 {
		return 0
	}

	var st []int
	ret := 0

	for i := 0; i <= n; i++ {
		var cur int
		if i == n {
			cur = -1
		} else {
			cur = height[i]
		}

		for len(st) != 0 && height[st[len(st)-1]] > cur {
			h := height[st[len(st)-1]]
			st = st[:len(st)-1]
			var w int
			if len(st) == 0 {
				w = i
			} else {
				w = i - st[len(st)-1] - 1
			}
			ret = max(ret, h*w)
		}
		st = append(st, i)
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func reverse(a *[]int) {
	n := len(*a)
	l := 0
	r := n - 1
	for l < r {
		(*a)[l], (*a)[r] = (*a)[r], (*a)[l]
		l++
		r--
	}
	return
}

func main() {
	//a := []int{2, 1, 5, 6, 2, 3}
	a := []int{1, 1}
	fmt.Println(largestRectangleArea(a))
}
