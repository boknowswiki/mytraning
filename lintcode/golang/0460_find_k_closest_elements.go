/**
 * @param A: an integer array
 * @param target: An integer
 * @param k: An integer
 * @return: an integer array
 */
func kClosestNumbers (A []int, target int, k int) []int {
    // write your code here
    var ret []int
    ret = []int{}
    n := len(A)
    if n == 0 {
        return ret
    }
    
    if k == 0 {
        return ret
    }
    
    l := 0
    r := n-1
    
    for l + 1 < r {
        mid := (l+r)/2
        if A[mid] >= target {
            r = mid
        } else {
            l = mid
        }
    }
    
    for k > 0 {
        if l >= 0 && r < n {
            if abs(A[l] - target) <= abs(A[r] - target) {
                ret = append(ret, A[l])
                l -= 1
            } else {
                ret = append(ret, A[r])
                r += 1
            }
        } else if l < 0 {
            ret = append(ret, A[r])
            r += 1
        } else {
            ret = append(ret, A[l])
            l -= 1
        }
        k -= 1
    }
    
    return ret
}

func abs (a int) int {
    if a < 0 {
        return -a
    }
    
    return a
}
