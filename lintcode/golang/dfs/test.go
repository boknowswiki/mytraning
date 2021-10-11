package main

// dfs

import (
	"fmt"
	"math"
)

// segment tree

/**
 * @param n: An integer
 * @return: a list of combination
 */
func getFactors(n int) [][]int {
	// write your code here
	ret := [][]int{}
	dfs(n, 2, []int{}, &ret)
	return ret
}

func dfs(remain int, start int, path []int, ret *[][]int) {
	if remain == 1 && len(path) != 1 {
		tmp := make([]int, len(path))
		copy(tmp, path)
		*ret = append(*ret, tmp)
		return
	}

	for i := start; i < int(math.Sqrt(float64(remain)))+1; i++ {
		if remain%i == 0 {
			path = append(path, i)
			dfs(remain/i, i, path, ret)
			path = path[:len(path)-1]
		}
	}
	if remain >= start {
		path = append(path, remain)
		dfs(1, remain, path, ret)
		path = path[:len(path)-1]
	}
	return
}

func main() {
	a := 8
	fmt.Println(getFactors(a))
}
