/**
 * @param S: a string
 * @return: a list of integers representing the size of these parts
 */
func partitionLabels (S string) []int {
    // Write your code here
    m := make(map[byte]int)
    
    for i := 0; i < len(S); i++ {
        m[S[i]] = i
    }
    
    left, right := 0, 0
    ret := []int{}
    
    for i := 0; i < len(S); i++ {
        right = max(right, m[S[i]])
        if right == i {
            ret = append(ret, (right-left+1))
            left = i+1
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
