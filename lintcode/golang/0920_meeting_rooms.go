package main

//sweep line

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
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param intervals: an array of meeting time intervals
 * @return: if a person could attend all meetings
 */
func canAttendMeetings(intervals []*Interval) bool {
	// Write your code here
	n := len(intervals)
	if n == 0 {
		return false
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start ||
			(intervals[i].Start == intervals[j].Start && intervals[i].End < intervals[j].End)
	})

	for i := 1; i < n; i++ {
		if intervals[i].Start < intervals[i-1].End {
			return false
		}
	}

	return true

}

func main() {
	a := []*Interval{
		&Interval{0, 30},
		&Interval{5, 10},
		&Interval{15, 20},
	}
	fmt.Println(canAttendMeetings(a))
}


/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

/**
 * @param intervals: an array of meeting time intervals
 * @return: if a person could attend all meetings
 */
import "sort"
//import "fmt"

func canAttendMeetings (intervals []*Interval) bool {
    // Write your code here
    sort.Slice(intervals, func(i int, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})
	/*
	for _, i := range intervals {
	    fmt.Println(i.Start, i.End)
	}*/

	for i := 0; i < len(intervals)-1; i++ {
	    /*
		if intervals[i].Start <= intervals[i+1].Start &&
			intervals[i].End >= intervals[i+1].End {
			return false
		}
		*/
		if intervals[i].End > intervals[i+1].Start {
		    return false
		}
	}
	return true
}
