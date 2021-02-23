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
