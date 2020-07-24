/**
 * @param A: an array
 * @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
 */
func peakIndexInMountainArray (A []int) int {
    // Write your code here
    n := len(A)
    l := 1
    r := n-2
    
    for l+1 < r {
        mid := (l+r)/2
        if A[mid] > A[mid-1] && A[mid] > A[mid+1] {
            return mid
        } else if A[mid] > A[mid-1] && A[mid] < A[mid+1] {
            l = mid
        } else {
            r = mid
        }
    }
    
    if A[l] > A[l+1] && A[l] > A[l-1] {
        return l
    }
    
    return r
}

