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
