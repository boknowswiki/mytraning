package main

import (
	"container/heap"
	"fmt"
	"sort"
)

type Point struct {
	X, Y int
}

type Node struct {
	val int
	X   int
	Y   int
}

type IntHeap []*Node

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].val < h[j].val }
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
 * @param points: a list of points
 * @param origin: a point
 * @param k: An integer
 * @return: the k closest points
 */
func kClosest(points []*Point, origin *Point, k int) []*Point {
	// write your code here
	maxHeap := &IntHeap{}

	for _, p := range points {
		dist := getDist(p, origin)
		heap.Push(maxHeap, &Node{val: -dist, X: p.X, Y: p.Y})
		if maxHeap.Len() > k {
			heap.Pop(maxHeap)
		}
	}

	ret := []*Point{}
	for maxHeap.Len() > 0 {
		node := heap.Pop(maxHeap).(*Node)
		ret = append(ret, &Point{X: node.X, Y: node.Y})
		//ret = append([]*Point{&Point{X: node.X, Y: node.Y}}, ret...)
	}

	sort.Slice(ret, func(i, j int) bool {
		d1 := (ret[i].X-0)*(ret[i].X-0) + (ret[i].Y-0)*(ret[i].Y-0)
		d2 := (ret[j].X-0)*(ret[j].X-0) + (ret[j].Y-0)*(ret[j].Y-0)
		return d1 < d2 || (d1 == d2 && ret[i].X < ret[j].X) || (d1 == d2 && ret[i].X == ret[j].X && ret[i].Y < ret[j].Y)
	})

	return ret
}

func getDist(p, o *Point) int {
	return (p.X-o.X)*(p.X-o.X) + (p.Y-o.Y)*(p.Y-o.Y)
}

func main() {
	r := []int{10, 20, 30, 40}
	g := [][]int{
		[]int{1, 3},
		[]int{0, 2},
		[]int{1},
		[]int{0},
	}
	s := 0
	k := 2

	fmt.Println(topKMovie(r, g, s, k))
}
