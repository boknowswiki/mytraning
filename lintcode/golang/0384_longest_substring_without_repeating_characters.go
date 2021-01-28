
/**
 * @param s: a string
 * @return: an integer
 */

//import "fmt"

func lengthOfLongestSubstring (s string) int {
    // write your code here
    n := len(s)
    if n == 0 {
        return 0
    }
    
    m := make(map[byte]int)
    l := 0
    ret := 0
    
    for r := 0; r < n; r++ {
        //fmt.Println(l, s[l], r, s[r], m)
        c := s[r]
        _, ok := m[c]
        for l < r && ok {
            m[s[l]]--
            if m[s[l]] == 0 {
                delete(m, s[l])
            }
            l++
            _, ok = m[c]
        }
        //fmt.Printf("l %v, r %v\n", l, r)
        if val, ok := m[c]; !ok {
            m[c] = 1
        } else {
            m[c] = val+1
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


/**
 * @param s: a string
 * @return: an integer
 */
func lengthOfLongestSubstring (s string) int {
    // write your code here
    n := len(s)
    if n == 0 {
        return 0
    }
    
    m := [256]int{}
    j := 0
    ret := 0
    for i := 0; i < len(s); i++ {
        for j < len(s) && m[s[j]] == 0 {
            m[s[j]] = 1 
            ret = maxnum(ret, j - i + 1)
            j++
        }
        m[s[i]] = 0
    }
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

