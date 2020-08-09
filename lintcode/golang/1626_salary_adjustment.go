
/**
 * @param a: the list of salary
 * @param target: the target of the sum
 * @return: the cap it should be
 */
 
import "sort"

func getCap (a []int, target int) int {
    // Write your code here.
    n := len(a)
    if n == 0 {
        return target
    }
    
    sort.Ints(a)
    
    l := a[0]
    r := target/n + 1
    
    for l + 1 < r {
        mid := (l+r)/2
        val := getVal(a, mid)
        
        if val == target {
            return mid
        } else if val < target {
            l = mid
        } else {
            r = mid
        }
    }
    
    if getVal(a, l) >= target {
        return l
    }
    
    return r
}

func getVal (a []int, c int) int {
    var ret int
    
    for _, v := range(a) {
        if v < c {
            ret += c
        } else {
            ret += v
        }
    }
    
    return ret
}
