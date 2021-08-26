package main

import (
	"fmt"
	"sort"
)

type Intervals []*Interval

func (a Intervals) Len() int { return len(a) }
func (a Intervals) Less(i, j int) bool {
	if (*a[i]).Start < (*a[j]).Start {
		return true
	}
	if a[i].Start == a[j].Start && a[i].End < a[j].End {
		return true
	}
	return false
}
func (a Intervals) Swap(i, j int) { a[i], a[j] = a[j], a[i] }

/**
 * Definition of Interval:
 */
type Interval struct {
	Start, End int
}

/**
 * @param intervals: interval list.
 * @return: A new interval list.
 */
func merge(intervals []*Interval) []*Interval {
	// write your code here
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start ||
			(intervals[i].Start == intervals[j].Start && intervals[i].End < intervals[j].End)
	})
	var ret []*Interval
	if len(intervals) == 0 {
		return intervals
	}
	ret = append(ret, intervals[0])
	for i := 1; i < len(intervals); i++ {
		if intervals[i].End < ret[len(ret)-1].End {
			continue
		}
		if intervals[i].Start <= ret[len(ret)-1].End &&
			intervals[i].End > ret[len(ret)-1].End {
			ret[len(ret)-1].End = intervals[i].End
		}
		if intervals[i].Start > ret[len(ret)-1].End {
			ret = append(ret, intervals[i])
		}
	}

	return ret
}

func main() {
	a := Interval{
		1,
		3,
	}
	b := []*Interval{
		&a,
	}
	fmt.Println(merge(b))
}
