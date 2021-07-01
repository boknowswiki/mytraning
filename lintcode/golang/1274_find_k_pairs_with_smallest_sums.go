//heap
// not ac, just ordering issue.


import (
	"container/heap"
    //"sort"
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

func newNode(val, r, c int) *Node {
	return &Node{
		val:   val,
		r: r,
        c: c,
	}
}

/**
 * @param nums1: List[int]
 * @param nums2: List[int]
 * @param k: an integer
 * @return: return List[List[int]]
 */
func kSmallestPairs (nums1 []int, nums2 []int, k int) [][]int {
    // write your code here
	m := len(nums1)
	n := len(nums2)
	ret := make([][]int, 0)
	v := make(map[int]bool)

	minHeap := &NodeHeap{}
	node := &Node{
		val: nums1[0] + nums2[0],
		r:   0,
		c:   0,
	}
	heap.Push(minHeap, node)
	v[0] = true

	for i := 0; i < min(k, m*n); i++ {
		node := heap.Pop(minHeap).(*Node)
		s := []int{nums1[(*node).r], nums2[(*node).c]}
		//sort.Ints(s)
		ret = append(ret, s)
		/*
			if nums1[(*node).r] < nums2[(*node).c] {
				ret = append(ret, []int{nums1[(*node).r], nums2[(*node).c]})
			} else {
				ret = append(ret, []int{nums2[(*node).c], nums1[(*node).r]})
			}
		*/

		if (*node).c+1 < n {
			index := ((*node).r)*n + ((*node).c + 1)
			if _, ok := v[index]; !ok {
				heap.Push(minHeap, &Node{
					val: nums1[(*node).r] + nums2[(*node).c+1],
					r:   (*node).r,
					c:   (*node).c + 1,
				})
				v[index] = true
			}
		}

		if (*node).r+1 < m {
			index := ((*node).r+1)*n + ((*node).c)
			if _, ok := v[index]; !ok {
				heap.Push(minHeap, &Node{
					val: nums1[(*node).r+1] + nums2[(*node).c],
					r:   (*node).r + 1,
					c:   (*node).c,
				})
				v[index] = true
			}
		}

	}

	return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
