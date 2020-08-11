/**
 * @param t: the length of the flight
 * @param dur: the length of movies 
 * @return: output the lengths of two movies
 */
 
import "sort"

func aerialMovie (t int, dur []int) []int {
    // Write your code here
    sort.Ints(dur)
    ret := make([]int, 2)
    t = t-30
    l := 0
    r := len(dur)-1
    tmp := 0
    
    for l < r {
        val := dur[l]+dur[r]
        if val > t {
            r -= 1
            continue
        }
        
        if val > tmp {
            tmp = val
            ret[0] = dur[l]
            ret[1] = dur[r]
        }
        
        l += 1
    }
    return ret
}
