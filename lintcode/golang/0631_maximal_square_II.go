package main

// dp
// time O(m*n) space O(m*n), space can be improved to O(m)

import (
	"fmt"
)

/**
/**
 * @param matrix: a matrix of 0 an 1
 * @return: an integer
*/
func maxSquare2(matrix [][]int) int {
	// write your code here
	// state: dp[i][j] is the number square at point(i, j), left[i][j] is the number zeros to the left of point(i, j), up[i][j] is number zeros to the up of point(i, j).
	// func: dp[i][j] = min(dp[i-1][j-1], left[i][j-1], up[i-i][j])+1
	// init: dp[i][j] = 0
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

	left := make([][]int, m)
	for i := 0; i < m; i++ {
		left[i] = make([]int, n)
	}
	up := make([][]int, m)
	for i := 0; i < m; i++ {
		up[i] = make([]int, n)
	}

	ret := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				dp[i][j] = 0
				left[i][j] = 1
				up[i][j] = 1
				if i > 0 {
					up[i][j] = up[i-1][j] + 1
				}
				if j > 0 {
					left[i][j] = left[i][j-1] + 1
				}
			} else {
				left[i][j] = 0
				up[i][j] = 0
				if i > 0 && j > 0 {
					dp[i][j] = min(dp[i-1][j-1], left[i][j-1], up[i-1][j]) + 1
				} else {
					dp[i][j] = 1
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
	a := [][]int{
		{1, 0, 1, 0, 0},
		{1, 0, 0, 1, 0},
		{1, 1, 0, 0, 1},
		{1, 0, 0, 1, 0},
	}
	fmt.Println(maxSquare2(a))
}
