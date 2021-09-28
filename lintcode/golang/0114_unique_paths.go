package main

import "fmt"

// dp

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * @param m: positive integer (1 <= m <= 100)
 * @param n: positive integer (1 <= n <= 100)
 * @return: An integer
 */
func uniquePaths(m int, n int) int {
	// write your code her
	// dp[i][j] means the number of paths at row i, col j.
	// dp[i][j] = dp[i-1][j] + dp[i][j-1]
	// dp[m-1][n-1] is the answer.

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] = 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}

	return dp[m-1][n-1]
}

func main() {
	fmt.Println(uniquePaths(3, 3))
}
