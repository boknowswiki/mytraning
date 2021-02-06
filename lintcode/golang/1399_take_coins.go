/**
 * @param list: The coins
 * @param k: The k
 * @return: The answer
 */
func takeCoins (list []int, k int) int {
    // Write your code here
    n := len(list)
    if n <= k {
        return sum(list)
    }
    
    l := -1
    r := -k
    
    all_right := sum(list[n+r:])
    ret := all_right
    
    for r != 0 {
        all_right -= list[n+r]
        r++
        l++
        all_right += list[l]
        ret = max(ret, all_right)
    }
    
    return ret
}

func sum(l []int) int {
    ret := 0
    
    for _, v := range l {
        ret += v
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
