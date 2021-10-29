package main

//sweep line

// time O(nlogn) due to the sort
// space O(n)

import (
	"fmt"
	"sort"
)

type Interval struct {
	Start, End int
}

type point struct {
	time int
	cnt  int
}

/**
 * @param airplanes: An interval array
 * @return: Count of airplanes are in the sky.
 */
func countOfAirplanes(airplanes []*Interval) int {
	// write your code here
	n := len(airplanes)
	if n == 0 {
		return 0
	}

	points := make([]*point, 0)

	for _, a := range airplanes {
		points = append(points, &point{time: a.Start, cnt: 1})
		points = append(points, &point{time: a.End, cnt: -1})
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i].time < points[j].time ||
			(points[i].time == points[j].time && points[i].cnt < points[j].cnt)
	})

	ret := 0
	cur := 0

	for _, p := range points {
		cur += p.cnt
		ret = max(ret, cur)
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []*Interval{
		&Interval{1, 10},
		&Interval{2, 3},
		&Interval{5, 8},
		&Interval{4, 7},
	}
	fmt.Println(countOfAirplanes(a))
}
