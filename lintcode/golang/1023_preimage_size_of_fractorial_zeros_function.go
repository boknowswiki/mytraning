/**
 * @param K: an integer
 * @return: how many non-negative integers x have the property that f(x) = K
 */

import "math"

func preimageSizeFZF (K int) int {
    // Write your code here
    l := 0
    r := math.MaxInt64
    
    for l  < r {
        mid := l + (r-l)/2
        cnt := getCnt(mid)
        if cnt < K {
            l = mid+1
        } else {
            r = mid
        }
    }
    
    if getCnt(l) == K {
        return 5 - l%5
    }
    return 0
}

func getCnt(n int) int {
    var cnt int
    for n > 0 {
        cnt += n/5
        n = n/5
    }
    
    return cnt
}
