
//https://www.cnblogs.com/yuzhangcmu/p/4200096.html

/**
 * @param A: An array of integers
 * @return: An integer
 */
func firstMissingPositive (A []int) int {
    // write your code here
    if A == nil {
        return 0
    }
    n := len(A)
    
    for i := 0; i < n; i++ {
        for A[i] > 0 && A[i] <= n && A[A[i]-1] != A[i] {
            A[i], A[A[i]-1] = A[A[i]-1], A[i]
        }
    }
    
    for i := 0; i < n; i++ {
        if A[i] != i+1 {
            return i+1
        }
    }
    
    return n+1
}

