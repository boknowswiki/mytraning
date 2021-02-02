/**
 * @param nums:  an array of n integers
 * @param target: a target
 * @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
 */

import "sort"
func threeSumSmaller (nums []int, target int) int {
    // Write your code here
    n := len(nums)
    if n < 3 {
        return 0
    }
    
    sort.Ints(nums)
    ret := 0
    
    for i := 0; i < n-2; i++ {
        j := i+1
        k := n-1
        
        for j < k {
            val := nums[i]+nums[j]+nums[k]
            if val < target {
                ret += k-j
                j++
            } else {
                k--
            }
        }
    }
    
    return ret
}

