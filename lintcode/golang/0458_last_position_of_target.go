/**
 * @param nums: An integer array sorted in ascending order
 * @param target: An integer
 * @return: An integer
 */
func lastPosition (nums []int, target int) int {
    // write your code here
    n := len(nums)
    if n == 0 {
        return -1
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        if nums[mid] <= target {
            l = mid
        } else {
            r = mid
        }
    }
    
    if nums[r] == target {
        return r
    }
    if nums[l] == target {
        return l
    }
    
    return -1
}

