package main

import (
	"container/heap"
	"fmt"
)

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

/**
 * @param n: a positive integer
 * @param primes: the given prime list
 * @return: the nth super ugly number
 */
func nthSuperUglyNumber(n int, primes []int) int {
	// write your code here
	hq := &IntHeap{1}
	v := make(map[int]bool)
	v[1] = true

	for i := 1; i < n; i++ {
		multi := heap.Pop(hq).(int)
		for _, num := range primes {
			newNum := multi * num
			if !v[newNum] {
				v[newNum] = true
				heap.Push(hq, newNum)
			}
		}
	}

	return heap.Pop(hq).(int)
}

func main() {
	n := 6
	nums := []int{2, 7, 13, 19}

	fmt.Println(nthSuperUglyNumber(n, nums))
}

