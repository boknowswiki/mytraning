/**
 * @param s: A string
 * @param k: An integer
 * @return: An integer
 */
func lengthOfLongestSubstringKDistinct (s string, k int) int {
    // write your code here
    n := len(s)
    if n < k {
        return n
    }
    
    m := make(map[byte]int)
    l := 0
    ret := 0
    
    for i := 0; i < n; i++ {
        c := s[i]
        if _, ok := m[c]; !ok {
            m[c] = 1
        } else {
            m[c]++
        }
        
        for len(m) > k {
            rc := s[l]
            m[rc]--
            if m[rc] == 0 {
                delete(m, rc)
            }
            l++
        }
        
        ret = max(ret, i-l+1)
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
