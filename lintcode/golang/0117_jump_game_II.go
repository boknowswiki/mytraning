
//greedy

/**
 * @param A: A list of integers
 * @return: An integer
 */
 
const MaxInt = int((^uint(0))>>1)
 
func jump (A []int) int {
    // write your code here
    n := len(A)
    
    start, end, jumps := 0, 0, 0
    farest := 0
    
    for end < n-1 {
        jumps++
        farest = end
        
        for i := start; i <= end; i++ {
            if A[i]+i > farest {
                farest = A[i]+i
            }
        }
        start = end+1
        end = farest
    }
    
    return jumps
}


// ETL
// dp


/**
 * @param A: A list of integers
 * @return: An integer
 */
func jump(A []int) int {
	// write your code here
	// state: dp[i] the minimum step at ith index.
	// func: dp[i] = min(dp[i], dp[j]+1) j from 0 to i.
	// init: dp[i] = maxInt, dp[0] = 0
	// result: dp[n-1]

	n := len(A)
	if n == 0 {
		return 0
	}

	dp := make([]int, n)
	dp[0] = 0

	for i := 1; i < n; i++ {
		dp[i] = MaxInt
		for j := 0; j < i; j++ {
			if dp[j] != MaxInt && A[j]+j >= i {
				dp[i] = min(dp[i], dp[j]+1)
			}
		}
	}

	return dp[n-1]
}

/**
 * @param A: A list of integers
 * @return: An integer
 */
 
const MaxInt = int((^uint(0))>>1)
 
func jump (A []int) int {
    // write your code here
    n := len(A)
    dp := make(map[int]int, n)
    
    dp[0] = 0
    
    for i := 1; i < n; i++ {
        dp[i] = MaxInt
        for j := 0; j < i; j++ {
            if dp[j] != MaxInt && A[j] + j >= i {
                dp[i] = min(dp[i], dp[j]+1)
            }
        }
    }
    
    return dp[n-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

