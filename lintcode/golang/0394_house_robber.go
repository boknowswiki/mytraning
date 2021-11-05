package main

// dp
// time O(n), space O(n)

import (
	"fmt"
)

/**
 * @param A: An array of non-negative integers
 * @return: The maximum amount of money you can rob tonight
 */
func houseRobber(A []int) int64 {
	// write your code here
	// dp[i] the max amount money at ith house.
	// dp[i] = max(dp[i-1], dp[i-2]+a[i])
	// dp[0] = a[0], dp[1] = max(a[0], a[1])
	// result is dp[n]
	n := len(A)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return int64(A[0])
	}

	dp := make([]int, n)
	dp[0] = A[0]
	dp[1] = max(A[0], A[1])
	for i := 2; i < n; i++ {
		dp[i] = max(dp[i-1], dp[i-2]+A[i])
	}

	return int64(dp[n-1])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	//a := []int{3, 8, 4}
	a := []int{5, 2, 1, 3}
	fmt.Println(houseRobber(a))
}
