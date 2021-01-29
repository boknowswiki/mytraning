/**
 * @param nums: an array of integer
 * @param target: an integer
 * @return: an integer
 */

import "sort"

func twoSum5 (nums []int, target int) int {
    // write your code here
    sort.Ints(nums)
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    ret := 0
    l := 0
    r := n-1
    
    for l < r {
        val := nums[l]+nums[r]
        if val <= target {
            ret += r-l
            l++
        } else {
            r--
        }
    }
    
    return ret
}

