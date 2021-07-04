
// heap
// not ac, but should correct.

package main


import (
	"container/heap"
	//"fmt"
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

/**
 * @param arr: The K spaced array
 * @param k: The param k
 * @return: Return the sorted array
 */
func getSortedArray(arr []int, k int) []int {
	// Write your code here
	n := len(arr)
	if n == 0 || n < k {
		return arr
	}

	minHeap := &NodeHeap{}
	ret := []int{}

	//heap.Push(minHeap, newNode(arr[0], 0, 1))
	for i := 0; i < k; i++ {

		heap.Push(minHeap, newNode(arr[i], i))
	}

    /*
	for i := 0; i < minHeap.Len(); i++ {
		fmt.Println([]*Node(*minHeap)[i])
	}
    */

	for minHeap.Len() > 0 {
		node := heap.Pop(minHeap).(*Node)
		//fmt.Println("pop: ", node)
		ret = append(ret, node.val)
		if node.index+k < n {
			heap.Push(minHeap, newNode(arr[node.index+k], node.index+k))
		}
	}

	return ret
}

func main() {
	n := []int{1, 2, 3}
	k := 1
	n = []int{4, 0, 5, 3, 10}
	k = 2
	n = []int{609807925, 45594341, 686473906, 25451741, 523752475, 1280974215, 221029645, 723695200, 80426861, 929520487, 1358492955, 752886693, 725157808, 155367191, 1606786341, 1530330315, 1249677092, 1788308819, 220871135, 1801214707, 1792471865, 1693881122, 2011270475, 222276059, 1888082805, 2070724378, 1854031060}
	k = 5

	fmt.Println(getSortedArray(n, k))
}
