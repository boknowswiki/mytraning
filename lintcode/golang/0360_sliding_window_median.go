package main

// heap, ac works!
//time O(nlogn)

import (
	"container/heap"
	"fmt"
)

type Node struct {
	val   int
	index int
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
 * @param nums: A list of integers
 * @param k: An integer
 * @return: The median of the element inside the window at each moving
 */
func medianSlidingWindow(nums []int, k int) []int {
	// write your code here
	n := len(nums)
	if n == 0 || n < k || k == 0 {
		return []int{}
	}

	var ret []int
	minH := &MinHeap{}
	maxH := &MinHeap{}
	mid := 0

	for i, val := range nums[:k] {
		heap.Push(maxH, &Node{val: -val, index: i})
	}

	for i := k / 2; i >= 0; i-- {
		node := heap.Pop(maxH).(*Node)
		node.val = -node.val
		heap.Push(minH, node)
	}

	for maxH.Len() > minH.Len()+1 {
		node := heap.Pop(maxH).(*Node)
		node.val = -node.val
		heap.Push(minH, node)
	}
	for minH.Len() > maxH.Len() {
		node := heap.Pop(minH).(*Node)
		node.val = -node.val
		heap.Push(maxH, node)
	}

	mid = -(*maxH)[0].val

	ret = append(ret, mid)

	for i := k; i < n; i++ {
		fmt.Println("mid is ", mid)
		if nums[i] <= mid {
			heap.Push(maxH, &Node{val: -nums[i], index: i})
		} else {
			heap.Push(minH, &Node{val: nums[i], index: i})
		}

		if nums[i-k] <= mid {
			index := getIndex(maxH, true, nums[i-k])
			if index == -1 {
				panic("max not find num")
			}
			heap.Remove(maxH, index)
		} else {
			index := getIndex(minH, false, nums[i-k])
			if index == -1 {
				panic("min not find num")
			}
			heap.Remove(minH, index)
		}

		for maxH.Len() > minH.Len()+1 {
			node := heap.Pop(maxH).(*Node)
			node.val = -node.val
			heap.Push(minH, node)
		}
		for minH.Len() > maxH.Len() {
			node := heap.Pop(minH).(*Node)
			node.val = -node.val
			heap.Push(maxH, node)
		}
		mid = -(*maxH)[0].val
		ret = append(ret, mid)
	}

	return ret
}

func getIndex(a *MinHeap, negtived bool, target int) int {
	for i := 0; i < a.Len(); i++ {
		if negtived {
			if (*a)[i].val == -target {
				return i
			}
		} else {
			if (*a)[i].val == target {
				return i
			}
		}
	}
	return -1
}

func main() {
	a := []int{
		1, 2, 7, 8, 5,
	}
	k := 3
	fmt.Println(medianSlidingWindow(a, k))
}



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

func getIndex(h *NodeHeap, max bool, target int) int {

	for i := 0; i < h.Len(); i++ {

		if max {
			if -[]*Node(*h)[i].val == target {
				return i
			}
		} else {
			if []*Node(*h)[i].val == target {
				return i
			}
		}
	}

	return -1
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
	//fmt.Println("max:")
	//printHeap(maxH)

	for i := k/2 - 1; i >= 0; i-- {
		//fmt.Println("i is ", i)
		node := heap.Pop(maxH)
		node.(*Node).val = -node.(*Node).val
		heap.Push(minH, node)
	}
	//fmt.Println("min:")
	//printHeap(minH)
	//fmt.Println("max:")
	//printHeap(maxH)

	ret = append(ret, -[]*Node(*maxH)[0].val)
	//fmt.Println("start ret is ", ret)

	for i := k; i < n; i++ {
		mid = ret[len(ret)-1]
		//fmt.Println("mid is ", mid, "at index: ", i)
		if nums[i] > mid {
			heap.Push(minH, newNode(nums[i], i))
			/*
				if nums[i-k] <= mid {
					node := heap.Pop(minH)
					node.(*Node).val = -node.(*Node).val
					heap.Push(maxH, node)
				}
			*/
		} else {
			heap.Push(maxH, newNode(-nums[i], i))
			/*
				if nums[i-k] >= mid {
					node := heap.Pop(maxH)
					node.(*Node).val = -node.(*Node).val
					heap.Push(minH, node)
				}
			*/
		}

		//fmt.Println("loop min:")
		//printHeap(minH)
		//fmt.Println("loop max:")
		//printHeap(maxH)
		//fmt.Println("finding: ", nums[i-k])

		if nums[i-k] <= mid {
			hIndex := getIndex(maxH, true, nums[i-k])
			if hIndex == -1 {
				panic("max find num error")
			}
			heap.Remove(maxH, hIndex)
		} else {
			hIndex := getIndex(minH, false, nums[i-k])
			if hIndex == -1 {
				panic("min find num error")
			}
			heap.Remove(minH, hIndex)
		}

		for maxH.Len() > minH.Len()+1 {
			node := heap.Pop(maxH)
			node.(*Node).val = -node.(*Node).val
			heap.Push(minH, node)
		}
		for minH.Len() > maxH.Len() {
			node := heap.Pop(minH)
			node.(*Node).val = -node.(*Node).val
			heap.Push(maxH, node)
		}
		ret = append(ret, -[]*Node(*maxH)[0].val)
	}

	return ret
}

