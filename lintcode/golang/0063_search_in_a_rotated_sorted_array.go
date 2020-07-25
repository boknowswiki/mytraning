/**
 * @param A: an integer ratated sorted array and duplicates are allowed
 * @param target: An integer
 * @return: a boolean 
 */
func search (A []int, target int) bool {
    // write your code here
    n := len(A)
    if n == 0 {
        return false
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        
        if A[mid] == target {
            return true
        }

        if A[mid] > A[l] {
            if target >= A[l] && target < A[mid] {
                r = mid
            } else {
                l = mid
            }
        } else if A[mid] < A[l] {
            if target > A[mid] && target <= A[r] {
                l = mid
            } else {
                r = mid
            }
        }
        l += 1
    }
    
    if A[l] == target {
        return true
    }
    if A[r] == target {
        return true
    }
    
    return false
}
