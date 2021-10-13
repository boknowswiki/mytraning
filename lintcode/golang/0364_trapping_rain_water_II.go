package main

// heap time mnlog(m+n)

import (
	"container/heap"
	"fmt"
)

type locate struct {
	x int
	y int
}

type Node struct {
	val int
	x   int
	y   int
}

// An IntHeap is a min-heap of ints.
type NodeHeap []*Node

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].val < h[j].val }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(*Node))
}

func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

/**
 * @param heights: a matrix of integers
 * @return: an integer
 */
func trapRainWater(heights [][]int) int {
	// write your code here
	minHp := &NodeHeap{}
	v := make(map[locate]bool)
	m := len(heights)
	n := len(heights[0])
	var ret int

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || i == m-1 || j == 0 || j == n-1 {
				heap.Push(minHp, &Node{heights[i][j], i, j})
				v[locate{i, j}] = true
			}
		}
	}

	dir := []struct {
		dx int
		dy int
	}{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for minHp.Len() != 0 {
		node := heap.Pop(minHp).(*Node)
		for i := 0; i < len(dir); i++ {
			cx := dir[i].dx + node.x
			cy := dir[i].dy + node.y
			if cx >= 0 && cx < m && cy >= 0 && cy < n && v[locate{cx, cy}] == false {
				maxHeight := max(node.val, heights[cx][cy])
				ret += maxHeight - heights[cx][cy]
				heap.Push(minHp, &Node{maxHeight, cx, cy})
				v[locate{cx, cy}] = true

			}

		}
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	a := [][]int{
		{12, 13, 0, 12},
		{13, 4, 13, 12},
		{13, 8, 10, 12},
		{12, 13, 12, 12},
		{13, 13, 13, 13},
	}
	fmt.Println(trapRainWater(a))
}



import (
	"container/heap"
	"fmt"
)

type Node struct {
	val int
	x   int
	y   int
}

type MinHeap []*Node

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].val < h[j].val }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(*Node))
}

func (h *MinHeap) Pop() interface{} {
	cur := *h
	n := len(cur)
	x := cur[n-1]
	*h = cur[:n-1]
	return x
}

/**
 * @param heights: a matrix of integers
 * @return: an integer
 */
func trapRainWater(heights [][]int) int {
	// write your code here
	m := len(heights)
	if m == 0 {
		return 0
	}
	n := len(heights[0])
	if n == 0 {
		return 0
	}
	minH := &MinHeap{}
	v := make([][]bool, m)
	for i := range v {
		v[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || i == m-1 || j == 0 || j == n-1 {
				heap.Push(minH, &Node{val: heights[i][j], x: i, y: j})
				v[i][j] = true
			}
		}
	}

	dir := []struct {
		dx int
		dy int
	}{
		{1, 0},
		{-1, 0},
		{0, 1},
		{0, -1},
	}

	ret := 0

	for minH.Len() != 0 {
		node := heap.Pop(minH).(*Node)
		for i := 0; i < len(dir); i++ {
			nx := dir[i].dx + node.x
			ny := dir[i].dy + node.y
			if nx >= 0 && nx < m && ny >= 0 && ny < n && !v[nx][ny] {
				maxH := max(node.val, heights[nx][ny])
				ret += maxH - heights[nx][ny]
				heap.Push(minH, &Node{val: maxH, x: nx, y: ny})
				v[nx][ny] = true
			}
		}
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
