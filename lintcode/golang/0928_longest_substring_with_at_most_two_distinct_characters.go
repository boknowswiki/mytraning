
// hash and two pointers

/**
 * @param s: a string
 * @return: the length of the longest substring T that contains at most 2 distinct characters
 */
func lengthOfLongestSubstringTwoDistinct (s string) int {
    // Write your code here
    n := len(s)
    if n <= 2 {
        return n
    }

    ret := 0
    l := 0
    d := make(map[byte]int)

    for r := 0; r < n; r++ {
        d[s[r]]++

        for len(d) > 2 {
            d[s[l]]--
            if d[s[l]] == 0 {
                delete(d, s[l])
            }
            l++
        }

        if len(d) == 2 {
            ret = max(ret, r-l+1)
        }
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
 * @return: the length of the longest substring T that contains at most 2 distinct characters
 */
func lengthOfLongestSubstringTwoDistinct (s string) int {
    // Write your code here
    m := make(map[byte]int)
    n := len(s)
    if n <= 2 {
        return n
    }
    
    l := 0
    ret := 0
    
    for r := 0; r < n; r++ {
        m[s[r]] += 1
        
        for l <= r && len(m) > 2 {
            m[s[l]]--
            if m[s[l]] == 0 {
                delete(m, s[l])
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
