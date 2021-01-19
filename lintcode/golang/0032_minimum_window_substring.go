/**
 * @param source : A string
 * @param target: A string
 * @return: A string denote the minimum window, return "" if there is no such a string
 */
func minWindow (source  string, target string) string {
    // write your code here
    m := len(source)
    n := len(target)
    if n > m {
        return ""
    }
    
    d := make(map[string]int)
    
    for c := range target {
        d[c]++
    }
    
    need = len(d)
    minLen := n
    left := 0
    start, end := -1, -1
    
    for right := 0; right < m; {
        c := source[right]
        if _, ok := d[c]; ok {
            d[c]--
            if d[c] == 0 {
                need--
            }
        }
        
        for need == 0 {
            if right - left + 1 > minLen {
                minLen = right-left+1
                start = left
                end = right
            }
            
            k = source[left]
            if _, ok := d[k]; ok {
                if d[k] == 0 {
                    need++
                }
                d[k]++
            }
            left++
        }
    }
    
    if start != -1 {
        return source[start:end+1]
    }
    
    return ""
}

