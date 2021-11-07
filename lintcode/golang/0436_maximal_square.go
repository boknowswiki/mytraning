package main

// dp
// time O(m*n) space O(m*n), space can be improved to O(m)

import (
	"fmt"
)

/**
 * @param matrix: a matrix of 0 and 1
 * @return: an integer
 */
func maxSquare(matrix [][]int) int {
	// write your code here
	// state: dp[i][j] is the largest square count at point (i, j)
	// function: dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
	// init: dp[i][j] == 1 if matrix[i][j] == 1
	// result: ret = max(ret, dp[i][j]*dp[i][j])

	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	if n == 0 {
		return 0
	}

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}

	ret := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = matrix[i][j]
			} else {
				if matrix[i][j] == 1 {
					dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
				}
			}
			ret = max(ret, dp[i][j])
		}
	}

	return ret * ret
}

func min(a, b, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
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
	/*
		a := [][]int{
			{1, 0, 1, 0, 0},
			{1, 0, 1, 1, 1},
			{1, 1, 1, 1, 1},
			{1, 0, 0, 1, 0},
		}
	*/
	a := [][]int{
		{0, 1, 0, 1, 1, 0},
		{1, 0, 1, 0, 1, 1},
		{1, 1, 1, 1, 1, 0},
		{1, 1, 1, 1, 1, 1},
		{0, 0, 1, 1, 1, 0},
		{1, 1, 1, 0, 1, 1},
	}
	fmt.Println(maxSquare(a))
}
