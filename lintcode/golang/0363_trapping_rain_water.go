
// 使用九章算法班中讲过的相向型双指针算法。
// 整个算法的思想是计算每个位置上可以盛放的水，累加起来。
// 
// 记录如下几个值：
// 
// left, right => 左右指针的位置
// left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height
// 每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。
// 与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：
// 
// 一种是 left_max > heights[left]，这种情况下，水可以盛放 left_max - heights[left] 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。
// 一种是 left_max <= heights[left]，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]
// left_max >= right_max 的情况类似处理。
// 
// 时间复杂度：O(n)O(n)，空间复杂度 O(1)O(1)

/**
 * @param heights: a list of integers
 * @return: a integer
 */

import "fmt"

func trapRainWater (heights []int) int {
    // write your code here
    l := 0
    r := len(heights)-1
    l_max, r_max := heights[l], heights[r]
    ret := 0
    
    for l <= r {
        fmt.Println(l,r, l_max, r_max, heights[l], heights[r])
        if l_max < r_max {
            l_max = max(l_max, heights[l])
            ret += l_max - heights[l]
            l++
        } else {
            r_max = max(r_max, heights[r])
            ret += r_max - heights[r]
            r--
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
