

// heap
// nlogn

import (
	"container/heap"
	"sort"
)

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
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param intervals: an array of meeting time intervals
 * @return: the minimum number of conference rooms required
 */
func minMeetingRooms(intervals []*Interval) int {
	// Write your code here
	if intervals == nil || len(intervals) == 0 {
		return 0
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start ||
			(intervals[i].Start == intervals[j].Start && intervals[i].End < intervals[j].End)
	})

	minHeap := &IntHeap{}
	heap.Push(minHeap, intervals[0].End)

	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start < []int(*minHeap)[0] {
			heap.Push(minHeap, intervals[i].End)
		} else {
			heap.Pop(minHeap)
			heap.Push(minHeap, intervals[i].End)
		}
	}

	return minHeap.Len()
}

/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param intervals: an array of meeting time intervals
 * @return: the minimum number of conference rooms required
 */


// sort with o(n)

import "sort"

type point struct {
    time int
    add int
}

func minMeetingRooms (intervals []*Interval) int {
    // Write your code here
    if len(intervals) == 0 {
        return 0
    }
    
    points := make([]point, 0)
    for _, interval := range intervals {
        points = append(points, point{time:interval.Start, add:1})
        points = append(points, point{time:interval.End, add:-1})
    }
    
    sort.Slice(points, func(i, j int) bool {
        return points[i].time < points[j].time
    })
    
    ret := 0
    ongoing := 0
    
    for _, p := range points {
        ongoing += p.add
        ret = max(ret, ongoing)
    }
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
