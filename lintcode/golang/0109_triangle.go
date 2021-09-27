package main

// dp

import "fmt"

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * @param triangle: a list of lists of integers
 * @return: An integer, minimum path sum
 */
func minimumTotal(triangle [][]int) int {
	// write your code here
	// dp[i][j] means at i row j col the minumum sum
	// dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
	// ret = min(dp[last row][j]) j is from 0 to last col.

	m := len(triangle)
	n := len(triangle[m-1])
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			dp[i][j] = MaxInt
		}
	}

	dp[0][0] = triangle[0][0]
	for i := 1; i < m; i++ {
		for j := 0; j < len(triangle[i]); j++ {
			if j == 0 {
				dp[i][j] = dp[i-1][j] + triangle[i][j]
			} else {
				dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
			}
		}
	}

	fmt.Println(dp)
	ret := dp[m-1][0]
	for j := 0; j < len(triangle[m-1]); j++ {
		ret = min(ret, dp[m-1][j])
	}
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	a := [][]int{{-1}, {2, 3}, {1, -1, -3}}
	fmt.Println(minimumTotal(a))
}
