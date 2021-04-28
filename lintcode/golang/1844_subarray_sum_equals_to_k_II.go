/**
 * @param nums: a list of integer
 * @param k: an integer
 * @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
 */

import "fmt"

func subarraySumEqualsKII (nums []int, k int) int {
    // write your code here
    n := len(nums)
    if n == 0 {
        return -1
    }

    preSum := make([]int, 0)
    preSum = append(preSum, 0)
    pre := 0
    ret := n

    for i := 0; i < n; i++ {
        pre += nums[i]
        preSum = append(preSum, pre)
    }

    fmt.Println(preSum)

    sum2Index := make(map[int]int)

    for i, _ := range nums {
        findVal := preSum[i+1] -k
        if val, ok := sum2Index[findVal]; ok {
            ret = min(ret, i+1-val)
        }
        sum2Index[preSum[i+1]] = i+1
    }

    if ret == n && sum(nums) < k {
        return -1
    }
    
    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func sum(nums []int) int {
    total := 0
    for _, num := range nums {
        total += num
    }

    return total
}
