/**
 * @param num: A list of integers
 * @return: An integer
 */
func longestConsecutive (num []int) int {
    // write your code here
    m := make(map[int]bool)
    for _, v := range num {
        m[v] = true
    }
    res, down, up := 1, 0, 0
    for k := range m {
        for i := k + 1; m[i]; i++ {
            up++
            delete(m, i)
        }
        for i := k - 1; m[i]; i-- {
            down++
            delete(m, i)
        }
        delete(m, k)
        if 1 + up + down > res {
            res = 1 + up + down
        }
        down, up = 0, 0
    }
    
    return res
}

