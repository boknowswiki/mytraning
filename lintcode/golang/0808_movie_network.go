
// heap + bfs + sort

import (
	"container/heap"
	"sort"
)

type Node struct {
	rate int
	num  int
}

type IntHeap []*Node

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].rate < h[j].rate }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(*Node))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

/**
 * @param rating: the rating of the movies
 * @param G: the realtionship of movies
 * @param S: the begin movie
 * @param K: top K rating
 * @return: the top k largest rating moive which contact with S
 */
func topKMovie(rating []int, G [][]int, S int, K int) []int {
	// Write your code here
	relatedM := getRelated(G, S)

	minHeap := &IntHeap{}
	ret := []int{}

	for _, m := range relatedM {
		heap.Push(minHeap, &Node{rate: rating[m], num: m})
		if minHeap.Len() > K {
			heap.Pop(minHeap)
		}
	}

	sort.Slice(*minHeap, func(i, j int) bool {
		return []*Node(*minHeap)[i].rate < []*Node(*minHeap)[j].rate
	})

	for _, node := range []*Node(*minHeap) {
		ret = append(ret, node.num)
	}

    sort.Ints(ret)
	return ret
}

func getRelated(g [][]int, s int) []int {
	v := make(map[int]bool)
	q := []int{}
	q = append(q, s)
	v[s] = true
	ret := []int{}

	for len(q) > 0 {
		m := q[0]
		q = q[1:]
		if m != s {
			ret = append(ret, m)
		}
		for _, nei := range g[m] {
			if v[nei] != true {
				q = append(q, nei)
				v[nei] = true
			}
		}
	}

	return ret
}
