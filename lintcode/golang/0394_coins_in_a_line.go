package main

// dp
// time O(n), space O(1) and space O(n)

import (
	"fmt"
)

// dp, time O(n), space O(n)

/**
 * @param n: An integer
 * @return: A boolean which equals to true if the first player will win
 */
func firstWillWin(n int) bool {
	// write your code here
	// state: dp[i] is first play will win at ith index.
	// func: dp[i] = !dp[i-1] || !dp[i-2]
	// init: dp[1] = true, dp[2] = true
	// result: dp[n]
	if n == 0 {
		return false
	}
	if n == 1 || n == 2 {
		return true
	}
	dp := make([]bool, n+1)
	dp[1] = true
	dp[2] = true
	for i := 3; i < n+1; i++ {
		dp[i] = !dp[i-1] || !dp[i-2]
	}

	return dp[n]
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
	a := 1
	a = 4
	fmt.Println(firstWillWin(a))
}
