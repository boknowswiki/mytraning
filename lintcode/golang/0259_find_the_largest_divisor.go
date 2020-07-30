/**
 * @param A: the array.
 * @param k: the integer.
 * @return: the divisor satisfy the requirement.
 */
func FindDivisor (A []int, k int) int {
    // 
    n := len(A)
    if n == 0 {
        return 0
    }
    
    l := 0
    r := 1<<32-1
    
    for l+1 < r {
        mid := (l+r)/2
        if helper(A, k, mid) {
            l = mid
        } else {
            r = mid
        }
    }
    
    if helper(A, k, l) {
        return l
    }
    
    return r
}

func helper(a []int, k, val int) bool {
    cnt := 0
    
    for _, v := range a {
        tmp := v/val
        if v%val != 0 {
            tmp += 1
        }
        cnt += tmp
    }
    
    return cnt >= k
}
