// heap

/**
 * @param n: An integer
 * @return: return a  integer as description.
 */

import "container/heap"

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func nthUglyNumber (n int) int {
    // write your code here
    factors := []int{2,3,5}
    h := &IntHeap{1}
    heap.Init(h)
    v := make(map[int]int)

    for i := 1; i < n; i++ {
        cur := heap.Pop(h)
        for j := 0; j < len(factors); j++ {
            num := cur.(int)*factors[j]
            if _, ok := v[num]; ok {
                continue
            }
            v[num] = num
            heap.Push(h, num)
        }
    }

    return heap.Pop(h).(int)
}

