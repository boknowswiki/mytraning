package main

// union find

import (
	"fmt"
)

type uf struct {
	father []int
	count  int
}

func newUF(n, c int) *uf {
	father := make([]int, n)
	for i := 0; i < n; i++ {
		father[i] = i
	}

	return &uf{
		father: father,
		count:  c,
	}
}

func (uf *uf) find(a int) int {
	if uf.father[a] == a {
		return a
	}

	return uf.find(uf.father[a])
}

func (uf *uf) union(a, b int) {
	fa := uf.find(a)
	fb := uf.find(b)
	if fa == fb {
		return
	}

	uf.father[fa] = fb
	uf.count--

	return
}

func (uf *uf) getCount() int {
	return uf.count
}

/**
 * @param grid: a boolean 2D matrix
 * @return: an integer
 */
func numIslands(grid [][]bool) int {
	// write your code here
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	if n == 0 {
		return 0
	}

	l := m * n
	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == true {
				count++
			}
		}
	}

	uf := newUF(l, count)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == false {
				continue
			}
			p := i*n + j
			if i > 0 && grid[i-1][j] == true {
				q := p - n
				uf.union(p, q)
			}
			if i < m-1 && grid[i+1][j] == true {
				q := p + n
				uf.union(p, q)
			}
			if j > 0 && grid[i][j-1] == true {
				q := p - 1
				uf.union(p, q)
			}
			if j < n-1 && grid[i][j+1] == true {
				q := p + 1
				uf.union(p, q)
			}
		}
	}

	return uf.getCount()
}

func main() {
	g := [][]int{
		{1, 1, 0, 0, 0},
		{0, 1, 0, 0, 1},
		{0, 0, 0, 1, 1},
		{0, 0, 0, 0, 0},
		{0, 0, 0, 0, 1},
	}
	fmt.Println(numIslands(g))
}
