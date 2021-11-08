package main

// dp
// time O(n), space O(1) and space O(n)

import (
	"fmt"
)

/**
 * @param A: An array of Integer
 * @return: an integer
 */
func longestIncreasingContinuousSubsequence(A []int) int {
	// write your code here
	// state: dp[i] is the longest increasing continues subsequence at ith index.
	// func: dp[i] =  dp[i-1]+1 if A[i] > A[i-1]
	// init: dp[i] = 1
	// result: ret = max(ret, dp[i])
	n := len(A)
	if n == 0 {
		return 0
	}

	ret := 1
	inc := 1
	dec := 1

	for i := 1; i < n; i++ {
		if A[i] > A[i-1] {
			inc++
			dec = 1
		} else {
			inc = 1
			dec++
		}
		ret = max3(ret, inc, dec)
	}
	/*
		// increasing
		dp := make([]int, n)
		dp[0] = 1
		for i := 1; i < n; i++ {
			if A[i] > A[i-1] {
				dp[i] = dp[i-1] + 1
			} else {
				dp[i] = 1
			}
			ret = max(dp[i], ret)
		}

		// decreasing
		dp[0] = 1
		for i := 1; i < n; i++ {
			if A[i] < A[i-1] {
				dp[i] = dp[i-1] + 1
			} else {
				dp[i] = 1
			}
			ret = max(dp[i], ret)
		}
	*/

	return ret
}

func max3(a, b, c int) int {
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	}

	return c
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []int{5, 4, 2, 1, 3}
	fmt.Println(longestIncreasingContinuousSubsequence(a))
}
