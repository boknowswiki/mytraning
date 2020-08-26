/**
 * @param A: the array
 * @param K: sum
 * @return: the length
 */
func shortestSubarray (A []int, K int) int {
    // Write your code here.
    n := len(A)
    preSum := make([]int, n+1)
    for i, v := range A {
        preSum[i+1] = preSum[i] + v
    }
    
    ret := n+1
    var q []int
    
    for i := 0; i < n+1; i++ {
        for len(q) != 0 && preSum[i] - preSum[q[0]] >= K {
            ret = min(ret, i-q[0])
            q = q[1:len(q)]
            
        }
        for len(q) != 0 && preSum[i] <= preSum[q[len(q)-1]] {
            q = q[:len(q)-1]
        }
        q = append(q, i)
    }
    
    if ret <= n {
        return ret
    }
    return -1
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
