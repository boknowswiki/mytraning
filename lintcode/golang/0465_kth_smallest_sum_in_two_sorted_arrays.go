package main

// heap

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
 * @param A: an integer arrays sorted in ascending order
 * @param B: an integer arrays sorted in ascending order
 * @param k: An integer
 * @return: An integer
 */
func kthSmallestSum(A []int, B []int, k int) int {
	// write your code here
	v := make(map[locate]bool)
	minHp := &NodeHeap{}
	m := len(A)
	n := len(B)
	ret := 0
	if k == 1 {
		return A[0] + B[0]
	}
	heap.Push(minHp, &Node{
		val: A[0] + B[0],
		x:   0,
		y:   0,
	})
	v[locate{x: 0, y: 0}] = true
	for i := 0; i < k; i++ {
		node := heap.Pop(minHp).(*Node)
		ret = node.val
		if node.x+1 < m && v[locate{x: node.x + 1, y: node.y}] == false {
			heap.Push(minHp, &Node{
				val: A[node.x+1] + B[node.y],
				x:   node.x + 1,
				y:   node.y,
			})
			v[locate{x: node.x + 1, y: node.y}] = true
		}
		if node.y+1 < n && v[locate{x: node.x, y: node.y + 1}] == false {
			heap.Push(minHp, &Node{
				val: A[node.x] + B[node.y+1],
				x:   node.x,
				y:   node.y + 1,
			})
			v[locate{x: node.x, y: node.y + 1}] = true
		}
	}
	return ret
}

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	a := []int{1, 7, 11}
	b := []int{2, 4, 6}
	k := 3
	fmt.Println(kthSmallestSum(a, b, k))
}
