//NOT AC, but should work.

/**
 * @param piles: an array
 * @param H: an integer
 * @return: the minimum integer K
 */
 
import "sort"
//import "fmt"

func minEatingSpeed (piles []int, H int) int {
    // Write your code here
    sort.Ints(piles)
    l := piles[0]
    r := piles[len(piles)-1]
    
    //fmt.Println(piles)
    for l+1 < r {
        mid := (l+r)/2
        val := getCnt(piles, mid)
        //fmt.Println(mid, val)
        if val <= H {
            r = mid
        } else {
            l = mid
        }
    }
    
    if getCnt(piles, l) <= H {
        return l
    }
    return r
}

func getCnt(piles []int, tartget int) int {
    var ret int
    
    for _, v := range piles {
        if v <= tartget {
            ret += 1
        } else {
            val := v/tartget
            if v%tartget != 0 {
                ret += 1
            }
            ret += val
        }
    }
    
    return ret
}
