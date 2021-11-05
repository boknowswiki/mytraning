package main

// dp time O(n), space O(1)

import (
	"fmt"
)

/**
 * @param nums: An array of non-negative integers.
 * @return: The maximum amount of money you can rob tonight
 */
func houseRobber2(nums []int) int {
	// write your code here
	// dp[i] is the max amount of money at ith house
	// dp[i] = max(dp[i-1], dp[i-2]+A[i]) for i from 0 to n-2 or 1 to n-1.
	// dp[0] = 0 or a[0]?
	// result = max(dp[n-1], dp[n-2])

	n := len(nums)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return nums[0]
	}

	ret := 0
	dp := make([]int, 2)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])
	// start from 0 to n-2
	for i := 2; i < n-1; i++ {
		dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2]+nums[i])
	}
	ret = dp[(n-2)%2]
	fmt.Println("after 1 is ", ret)

	// start from 1 to n-1
	dp = make([]int, 2)
	dp[0] = 0
	dp[1] = nums[1]
	for i := 2; i < n; i++ {
		dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2]+nums[i])
	}
	ret = max(ret, dp[(n-1)%2])

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []int{3, 6, 4}
	//a := []int{5, 2, 1, 3}
	fmt.Println(houseRobber2(a))
}
