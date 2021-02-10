/**
 * @param a: the array a
 * @return: return the maximum length
 */
func maxLen (a []int) int {
    // Write your code here
    m := make(map[int]int)
    n := len(a)
    if n <= 2 {
        return n
    }
    
    l := 0
    ret := 0
    
    for r := 0; r < n; r++ {
        m[a[r]] += 1
        
        for l <= r && len(m) > 2 {
            m[a[l]]--
            if m[a[l]] == 0 {
                delete(m, a[l])
            }
            l++
        }
        
        ret = max(ret, r-l+1)
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
