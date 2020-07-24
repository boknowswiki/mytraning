/**
 * @param houses: positions of houses
 * @param heaters: positions of heaters
 * @return: the minimum radius standard of heaters
 */
 
import "sort"
//import "fmt"

func findRadius (houses []int, heaters []int) int {
    // Write your code here
    sort.Ints(heaters)
    //fmt.Println(heaters)
    var ret int
    
    for _, h := range houses {
        ret = Max(ret, closest(heaters, h))
    }
    
    return ret
}

func closest(heaters []int, h int) int {
    l := 0
    r := len(heaters) -1
    
    for l + 1 < r {
        mid := (l+r)/2
        if heaters[mid] == h {
            return 0
        } else if heaters[mid] < h {
            l = mid
        } else {
            r = mid
        }
    }
    
    return Min(Abs(heaters[l]-h), Abs(heaters[r]-h))
}

func Max(x, y int) int {
    if x < y {
        return y
    }
    return x
}

// Min returns the smaller of x or y.
func Min(x, y int) int {
    if x > y {
        return y
    }
    return x
}

func Abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
