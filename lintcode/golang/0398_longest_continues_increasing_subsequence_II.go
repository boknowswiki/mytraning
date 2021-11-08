package main

// dp
// time O(n), space O(1) and space O(n)

import (
	"fmt"
)

// dp, time O(mn), space O(mn)

/**
 * @param matrix: A 2D-array of integers
 * @return: an integer
 */
func longestContinuousIncreasingSubsequence2(matrix [][]int) int {
	// write your code here
	// this dp is dfs with memorization.

	m := len(matrix)
	if m == 0 {
		return 0
	}
	n := len(matrix[0])
	if n == 0 {
		return 0
	}

	mem := make([][]int, m)
	for i := 0; i < m; i++ {
		mem[i] = make([]int, n)
	}

	ret := 1

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			ret = max(ret, dfs(matrix, m, n, i, j, mem))
		}
	}

	return ret
}

func dfs(maxtrix [][]int, m, n, x, y int, mem [][]int) int {
	if mem[x][y] != 0 {
		return mem[x][y]
	}
	dir := []struct {
		dx int
		dy int
	}{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	ret := 1

	for i := 0; i < len(dir); i++ {
		nx := dir[i].dx + x
		ny := dir[i].dy + y
		if isValid(m, n, nx, ny) && maxtrix[x][y] > maxtrix[nx][ny] {
			ret = max(ret, dfs(maxtrix, m, n, nx, ny, mem)+1)
		} else {
			continue
		}
	}
	mem[x][y] = ret
	return ret
}

func isValid(m, n, x, y int) bool {
	if x >= 0 && x < m && y >= 0 && y < n {
		return true
	}
	return false
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
	a := [][]int{
		{1, 2, 3, 4, 5},
		{16, 17, 24, 23, 6},
		{15, 18, 25, 22, 7},
		{14, 19, 20, 21, 8},
		{13, 12, 11, 10, 9},
	}
	fmt.Println(longestContinuousIncreasingSubsequence2(a))
}
