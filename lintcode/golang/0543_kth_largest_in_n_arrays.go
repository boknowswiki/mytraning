package main

// heap

import (
	"container/heap"
	"fmt"
	"sort"
)

type Node struct {
	val int
	r   int
	c   int
}

// An IntHeap is a max-heap of ints.
type NodeHeap []*Node

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].val > h[j].val }
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
 * @param arrays: a list of array
 * @param k: An integer
 * @return: an integer, K-th largest element in N arrays
 */
func KthInArrays(arrays [][]int, k int) int {
	// write your code here
	maxHP := &NodeHeap{}
	var ret int
	//m := len(arrays)
	for _, array := range arrays {
		//sort.Sort(sort.Reverse(sort.IntSlice{a}))
		sort.Slice(array, func(a, b int) bool {
			return array[b] < array[a]
		})
	}

	for i, array := range arrays {
		heap.Push(maxHP, &Node{
			val: array[0],
			r:   i,
			c:   0,
		})
	}

	for i := 0; i < k; i++ {
		node := heap.Pop(maxHP).(*Node)
		ret = node.val
		fmt.Println(ret, node)
		if node.c+1 < len(arrays[node.r]) {
			heap.Push(maxHP, &Node{
				val: arrays[node.r][node.c+1],
				r:   node.r,
				c:   node.c + 1,
			})
		}
	}
	return ret
}

// This example inserts several ints into an IntHeap, checks the minimum,
// and removes them in order of priority.
func main() {
	/*
		a := [][]int{
			{9, 3, 2, 4, 7},
			{1, 2, 3, 4, 8},
		}
		k := 3
	*/
	a := [][]int{
		{1, 7, 5, 10, 2},
	}
	k := 4
	fmt.Println(KthInArrays(a, k))
}
