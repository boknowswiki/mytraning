/**
 * @param n: An integer
 * @return: An integer which is the first bad version.
 */
func findFirstBadVersion (n int) int {
    // write your code here
    if n == 0 {
        return 0
    }
    
    l : = 0
    r := n-1
    
    for l + 1 < r {
        mid = (l+r)/2
        if isBadVErsion(mid) {
            r = mid
        } else {
            l = mid
        }
    }
    
    if isBadVErsion(l) {
        return l
    }
    
    return r
}

