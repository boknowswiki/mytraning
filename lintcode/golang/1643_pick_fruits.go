/**
 * @param arr: the arr
 * @return: the length of the longset subarray
 */
func pickFruits (arr []int) int {
    // Write your code here.
    n := len(arr)
    if n <= 2 {
        return n
    }
    ret := 0
    l := 0
    m := make(map[int]int)
    
    for r := 0; r < n; r++ {
        m[arr[r]]++
        for len(m) > 2 {
            m[arr[l]]--
            if m[arr[l]] == 0 {
                delete(m, arr[l])
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
