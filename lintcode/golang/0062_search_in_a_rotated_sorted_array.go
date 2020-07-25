/**
 * @param A: an integer rotated sorted array
 * @param target: an integer to be searched
 * @return: an integer
 */
func search (A []int, target int) int {
    // write your code here
    n := len(A)
    if n == 0 {
        return -1
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        
        if A[mid] > A[l] {
            if target >= A[l] && target < A[mid] {
                r = mid
            } else {
                l = mid
            }
        } else {
            if target > A[mid] && target <= A[r] {
                l = mid
            } else {
                r = mid
            }
        }
    }
    
    if A[l] == target {
        return l
    }
    if A[r] == target {
        return r
    }
    
    return -1
}
