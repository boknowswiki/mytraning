/**
 * @param A: an integer array sorted in ascending order
 * @param target: An integer
 * @return: an integer
 */

func closestNumber (A []int, target int) int {
    // write your code here
    n := len(A)
    if n == 0 {
        return -1
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        if A[mid] - target == 0 {
            return mid
        } else if A[mid] - target < 0 {
            l = mid
        } else {
            r = mid
        }
    }
    
    if Abs(A[l] - target) < Abs(A[r] - target) {
        return l
    }
    return r
}

func Abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
