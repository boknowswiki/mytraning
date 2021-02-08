/**
 * @param tree: The type of fruit
 * @return: The total amount of fruit you can collect.
 */
func totalFruit (tree []int) int {
    // write your code here
    m := make(map[int]int)
    n := len(tree)
    if n <= 2 {
        return n
    }
    
    l := 0
    ret := 0
    
    for r := 0; r < n; r++ {
        m[tree[r]] += 1
        
        for l <= r && len(m) > 2 {
            m[tree[l]]--
            if m[tree[l]] == 0 {
                delete(m, tree[l])
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
