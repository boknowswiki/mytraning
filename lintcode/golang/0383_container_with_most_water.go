

// 题意: 给定一个非负整数数组, 选取i, j使得 $|i-j| \times min(a[i], a[j])| 最大
// 
// 设定两个指针, 初始在两端, 计算这两个组成的容量, 然后移动值较小的那个, 所有计算结果取最大.
// 
// 可以反证法证明这样可以得到最优答案


/**
 * @param heights: a vector of integers
 * @return: an integer
 */
func maxArea (heights []int) int {
    // write your code here
    l := 0
    r := len(heights)-1
    ret := 0
    var water int
    
    for l < r {
        if heights[l] < heights[r] {
            water = heights[l] * (r-l)
            l++
        } else {
            water = heights[r] * (r-l)
            r--
        }
        
        ret = max(ret, water)
    }
    
    return ret
}

func max (a, b int) int {
    if a > b {
        return a
    }
    
    return b
}
