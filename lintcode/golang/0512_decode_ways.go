package main

// dp
// time O(n), space O(n)

import (
	"fmt"
)

/**
 * @param s: a string,  encoded message
 * @return: an integer, the number of ways decoding
 */
func numDecodings(s string) int {
	// write your code here
	// state: dp[i] is the number of ways decoding at ith index.
	// func: dp[i] = dp[i-1] if 0 < s[i] < 9 and dp[i-2] if 10 <= (s[i-2]*10+s[i-1]) <= 26, dp[i] += dp[i-2]
	// init: dp[0] = 1
	// result: dp[n]
	n := len(s)
	if n == 0 {
		return 0
	}

	dp := make([]int, n+1)
	dp[0] = 1

	for i := 1; i < n+1; i++ {
		if s[i-1] != '0' {
			dp[i] += dp[i-1]
		}
		if i >= 2 {
			val := int(s[i-2]-'0')*10 + int(s[i-1]-'0')
			if val >= 10 && val <= 26 {
				dp[i] += dp[i-2]
			}
		}
	}

	return dp[n]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
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
	a := "12"
	fmt.Println(numDecodings(a))
}
