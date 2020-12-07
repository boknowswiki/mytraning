
//greedy

/**
 * @param A: A list of integers
 * @return: A boolean
 */
func canJump (A []int) bool {
    // write your code here
    n := len(A)
    farest := A[0]
    
    for i := 1; i < n; i++ {
        if i <= farest && A[i]+i >= farest {
            farest = A[i]+i
        }
    }
    
    return farest >= n-1
}


//dp

/**
 * @param A: A list of integers
 * @return: A boolean
 */
func canJump (A []int) bool {
    // write your code here
    n := len(A)
    dp := make(map[int]bool, n)
    
    dp[0] = true
    
    for i := 1; i < n; i++ {
        dp[i] = false
        for j := 0; j < i; j++ {
            if dp[j] && A[j]+j >= i {
                dp[i] = true
            }
        }
    }
    
    return dp[n-1]
}

