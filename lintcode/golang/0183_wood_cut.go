/**
 * @param L: Given n pieces of wood with length L[i]
 * @param k: An integer
 * @return: The maximum length of the small pieces
 */

//import "fmt"

func woodCut (L []int, k int) int {
    // write your code here
    n := len(L)
    if n == 0 {
        return 0
    }
    
    if n == 1 && L[0] == 0 {
        return 0
    }
    //fmt.Printf("#v", L)
    
    l := 0
    r := max(L)
    
    for l + 1 < r {
        mid := (l+r)/2
        val := getCnt(L, mid)
        if val < k {
            r = mid
        } else {
            l = mid
        }
    }
    
    if getCnt(L, r) >= k {
        return r
    }
    return l
}

func max(l []int) int {
    var ret int
    for _, v := range l {
        if v > ret {
            ret = v
        }
    }
    
    return ret
}

func getCnt(l []int, target int) int {
    var ret int
    for _, v := range l {
        ret += v/target
    }
    return ret
}
