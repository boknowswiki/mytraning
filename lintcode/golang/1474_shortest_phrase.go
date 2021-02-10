/**
 * @param k: The number of words in the article
 * @param lim: TThe minimum number of words a phrase should contain 
 * @param str: The article
 * @return: Return the length of shortest phrase
 */

const MaxUint = ^uint(0) 
const MinUint = 0 
const MaxInt = int(MaxUint >> 1) 

func getLength (k int, lim int, str []string) int {
    // Write your code here
    s := make([]int, len(str))
    ret := MaxInt
    
    for i, w := range str {
        s[i] = len(w)
    }
    
    l := 0
    sum := 0
    
    for r := 0; r < len(s); r++ {
        sum += s[r]
        
        for r - l >= k && sum - s[l] >= lim {
            sum -= s[l]
            l++
        }
        
        if r - l + 1 >= k && sum >= lim {
            ret = min(ret, sum)
        }
        
    }
    
    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
