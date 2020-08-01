/**
 * @param pages: an array of integers
 * @param k: An integer
 * @return: an integer
 */
func copyBooks (pages []int, k int) int {
    // write your code here
    n := len(pages)
    if n == 0 {
        return 0
    }
    
    l := max(pages)
    r := sum(pages)
    
    for l + 1 < r {
        mid := (l+r)/2
        if helper(pages, mid) <= k {
            r = mid
        } else {
            l = mid
        }
    }
    
    if helper(pages, l) <= k {
        return l
    }
    
    return r
}

func max(p []int) int {
    var ret int
    for _, v := range p {
        if v > ret {
            ret = v
        }
    }
    return ret
}

func sum(p []int) int {
    var ret int
    for _, v := range p {
        ret += v
    }
    return ret
}

func helper(p []int, t int) int {
    var pp int
    var cnt int
    
    for _, v := range p {
        if pp + v > t {
            cnt += 1
            pp = 0
        }
        pp += v
    }
    
    if pp > 0 {
        cnt += 1
    }
    
    return cnt
}
