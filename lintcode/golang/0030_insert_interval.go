package main

//sweep line
// time O(n), space O(n)

import (
	"fmt"
)

type Interval struct {
	Start, End int
}

/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param intervals: Sorted interval list.
 * @param newInterval: new interval.
 * @return: A new interval list.
 */
func insert(intervals []*Interval, newInterval *Interval) []*Interval {
	// write your code here
	ret := make([]*Interval, 0)
	index := 0

	for _, inter := range intervals {
		if inter.End < newInterval.Start {
			ret = append(ret, inter)
			index++
		} else if inter.Start > newInterval.End {
			ret = append(ret, inter)
		} else {
			newInterval.Start = min(inter.Start, newInterval.Start)
			newInterval.End = max(inter.End, newInterval.End)
		}
	}

	ret = append(ret, nil)
	copy(ret[index+1:], ret[index:])
	ret[index] = newInterval
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []*Interval{
		&Interval{1, 2},
		&Interval{5, 9},
	}
	b := &Interval{2, 5}
	fmt.Println(insert(a, b))
}
