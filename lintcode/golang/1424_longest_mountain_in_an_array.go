/**
 * @param A: 
 * @return: the length of the longest mountain
 */
func longestMountain (A []int) int {
    // write your code here
    ret, up, down := 0, 0, 0
    
    for i := 1; i < len(A); i++ {
        if down >= 1 && A[i-1] < A[i] || A[i-1] == A[i] {
            up = 0
            down = 0
        }
        
        if A[i-1] < A[i] {
            up++
        }
        if A[i-1] > A[i] {
            down++
        }
        
        ret = max(ret, up+1+down)
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
