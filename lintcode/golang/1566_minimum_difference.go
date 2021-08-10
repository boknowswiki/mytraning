// heap

import (
	"container/heap"
    //"fmt"
)

type Node struct {
	val   int
	r int
    c int
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
 * @param array: a 2D array
 * @return: the minimum difference
 */
 func minimumDifference (array [][]int) int {
    // Write your code here
	minHeap := &NodeHeap{}
	var maxVal int
	var minDiff int
	maxVal = -1 << 31
	minDiff = 1<<31 - 1
	m := len(array)
	n := len(array[0])
	for i := 0; i < m; i++ {
		node := &Node{
			val: array[i][0],
			r: i,
			c: 0,
		}
		heap.Push(minHeap, node)
		maxVal = max(maxVal, array[i][0])
	}

	for minHeap.Len() != 0 {
		node := heap.Pop(minHeap).(*Node)
		minDiff = min(abs(maxVal-(*node).val), minDiff)
		if (*node).c == n-1 {
			break
		}
		maxVal = max(maxVal, array[(*node).r][(*node).c+1])
		newNode := &Node{
			val: array[(*node).r][(*node).c+1],
			r: (*node).r,
			c: (*node).c+1,
		}
		heap.Push(minHeap, newNode)
	}

	return minDiff
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
