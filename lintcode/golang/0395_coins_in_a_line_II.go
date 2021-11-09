package main

// dp
// time O(n), space O(n)

import (
	"fmt"
)

// dp, time O(n), space O(n)

/**
 * @param values: a vector of integers
 * @return: a boolean which equals to true if the first player will win
 */
func firstWillWin(values []int) bool {
	// write your code here
	// state: dp[i] is first play can take coin at ith index.
	// func: dp[i] = !dp[i-1] || !dp[i-2]
	// init: dp[0] = true, dp[1] = true, firstTotal + values[i] if dp[i] is true.
	// result: firstTotal > total/2

	n := len(values)

	firstTotal := 0
	if n == 0 {
		return false
	}
	if n == 1 || n == 2 {
		return true
	}
	dp := make([]bool, n)
	dp[0] = true
	dp[1] = true
	firstTotal += values[0]
	firstTotal += values[1]
	for i := 2; i < n; i++ {
		dp[i] = !dp[i-1] || !dp[i-2]
		if dp[i] {
			firstTotal += values[i]
		}
	}

	total := 0
	for i := 0; i < n; i++ {
		total += values[i]
	}

	return firstTotal > total/2
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
	//a := []int{1, 2, 2}
	a := []int{1, 2, 4}
	fmt.Println(firstWillWin(a))
}
