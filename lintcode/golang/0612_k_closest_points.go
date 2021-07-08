
// heap and sort

/**
 * Definition for a point.
 * type Point struct {
 *     X, Y int
 * }
 */

import (
    "container/heap"
    "sort"
)

type Node struct {
	val int
	X   int
	Y   int
}

type IntHeap []*Node

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].val < h[j].val || (h[i].val == h[j].val && h[i].X > h[j].X) || (h[i].val == h[j].val && h[i].X == h[j].X && h[i].Y > h[j].Y) }
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
func kClosest (points []*Point, origin *Point, k int) []*Point {
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
		ret = append([]*Point{&Point{X: node.X, Y: node.Y}}, ret...)
	}

    sort.Slice(ret, func(i, j int) bool {
		d1 := (ret[i].X-origin.X)*(ret[i].X-origin.X) + (ret[i].Y-origin.Y)*(ret[i].Y-origin.Y)
		d2 := (ret[j].X-origin.X)*(ret[j].X-origin.X) + (ret[j].Y-origin.Y)*(ret[j].Y-origin.Y)
		return d1 < d2 || (d1 == d2 && ret[i].X < ret[j].X) ||(d1 == d2 && ret[i].X == ret[j].X && ret[i].Y < ret[j].Y)
	})

	return ret
}

func getDist(p, o *Point) int {
    return (p.X-o.X)*(p.X-o.X) + (p.Y-o.Y)*(p.Y-o.Y)
}
