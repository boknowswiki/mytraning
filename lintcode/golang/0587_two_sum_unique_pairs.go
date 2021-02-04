/**
 * @param nums: an array of integer
 * @param target: An integer
 * @return: An integer
 */
 
import "sort"

func twoSum6 (nums []int, target int) int {
    // write your code here
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    sort.Ints(nums)
    
    l := 0
    r := n-1
    cnt := 0
    
    for l < r {
        for l < r && l != 0 && nums[l] == nums[l-1] {
            l++
        }
        
        for l < r && r != n-1 && nums[r] == nums[r+1] {
            r--
        }
        
        if l < r {
            val := nums[l] + nums[r]
            if val == target {
                cnt++
                l++
                r--
            } else if val < target {
                l++
            } else {
                r--
            }
        }
    }
    
    return cnt
}

