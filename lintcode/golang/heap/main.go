package main

// lintcode 360

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

func main() {
	//nums := []int{1, 2, 7, 8, 5}
	//k := 3
	//nums := []int{1, 2, 7, 7, 2}
	//k := 1
	//nums := []int{1, 2, 7, 7, 2, 10, 3, 4, 5}
	//k := 2

	nums := []int{76, 132, 106, 88, 187, 22, 76, 121, 187, 84, 53, 176, 9, 192, 22, 126, 127, 178, 26, 195, 142, 141, 4, 33, 112, 154, 127, 58, 90, 194, 80, 152, 178, 144, 110, 166, 169, 104, 120, 187, 89, 134, 118, 69, 5}
	k := 36

	ret := getMedian(nums, k)
	fmt.Println(ret)
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

func getMedian(nums []int, k int) []int {
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
	fmt.Println("max:")
	printHeap(maxH)

	for i := k/2 - 1; i >= 0; i-- {
		fmt.Println("i is ", i)
		node := heap.Pop(maxH)
		node.(*Node).val = -node.(*Node).val
		heap.Push(minH, node)
	}
	fmt.Println("min:")
	printHeap(minH)
	fmt.Println("max:")
	printHeap(maxH)

	ret = append(ret, -[]*Node(*maxH)[0].val)
	fmt.Println("start ret is ", ret)

	for i := k; i < n; i++ {
		mid = ret[len(ret)-1]
		fmt.Println("mid is ", mid, "at index: ", i)
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

		fmt.Println("loop min:")
		printHeap(minH)
		fmt.Println("loop max:")
		printHeap(maxH)
		fmt.Println("finding: ", nums[i-k])

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
