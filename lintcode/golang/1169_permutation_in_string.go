/**
 * @param s1: a string
 * @param s2: a string
 * @return: if s2 contains the permutation of s1
 */
func checkInclusion (s1 string, s2 string) bool {
    // write your code here
    n := len(s1)
    m := make(map[byte]int)
    
    for i, _ := range s1 {
        m[s1[i]]++
    }
    
    need := n
    
    for i, _ := range s2 {
        if val, ok := m[s2[i]]; ok {
            if val > 0 {
                need--
            }
            m[s2[i]] = val-1
        }
        
        if i >= n {
            if _, ok := m[s2[i-n]]; ok {
                m[s2[i-n]]++
                if m[s2[i-n]] > 0 {
                    need++
                }
            }
        }
        
        if need == 0 {
            return true
        }
    }
    
    return false
}
