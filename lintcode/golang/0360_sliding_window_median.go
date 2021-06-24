
// heap, not ac, but should correct.

import (
	"container/heap"
	"fmt"
)

type Node struct {
	val   int
	index int
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

func newNode(val, index int) *Node {
	return &Node{
		val:   val,
		index: index,
	}
}

func printHeap(h *NodeHeap) {
	n := len([]*Node(*h))
	for i := 0; i < n; i++ {
		fmt.Println([]*Node(*h)[i].val)
	}
}

/**
 * @param nums: A list of integers
 * @param k: An integer
 * @return: The median of the element inside the window at each moving
 */
func medianSlidingWindow (nums []int, k int) []int {
    // write your code here
    n := len(nums)
	if n == 0 || n < k || k == 0 {
		return []int{}
	}

	var ret []int
	maxH := &NodeHeap{}
	minH := &NodeHeap{}
	mid := 0

	for index, val := range nums[:k] {
		heap.Push(maxH, newNode(-val, index))
	}
	//printHeap(maxH)

	for i := k/2 - 1; i >= 0; i-- {
		//fmt.Println("i is ", i)
		node := heap.Pop(maxH)
		node.(*Node).val = -node.(*Node).val
		heap.Push(minH, node)
	}
	//printHeap(minH)

	//fmt.Printf("max %#v, min %#v\n", maxH, minH)
	ret = append(ret, -[]*Node(*maxH)[0].val)
	//fmt.Println("start ret is ", ret)

	for i := k; i < n; i++ {
		mid = ret[len(ret)-1]
		//fmt.Println("mid is ", mid, "at index: ", i)
		if nums[i] >= mid {
			heap.Push(minH, newNode(nums[i], i))
			if nums[i-k] <= mid {
				node := heap.Pop(minH)
				node.(*Node).val = -node.(*Node).val
				heap.Push(maxH, node)
			}
		} else {
			heap.Push(maxH, newNode(-nums[i], i))
			if nums[i-k] >= mid {
				node := heap.Pop(maxH)
				node.(*Node).val = -node.(*Node).val
				heap.Push(minH, node)
			}
		}

		for maxH.Len() > 0 && (i-k >= []*Node(*maxH)[0].index) {
			heap.Pop(maxH)
		}
		for minH.Len() > 0 && (i-k >= []*Node(*minH)[0].index) {
			heap.Pop(minH)
		}
		ret = append(ret, -[]*Node(*maxH)[0].val)
	}

	return ret
}

