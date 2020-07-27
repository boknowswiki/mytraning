/**
 * @param nums: a rotated sorted array
 * @return: the minimum number in the array
 */
func findMin (nums []int) int {
    // write your code here
    n := len(nums)
    
    if n == 0 {
        return 0
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        if nums[l] < nums[r] {
            return nums[l]
        } else {
            if nums[mid] > nums[l] {
                l = mid
            } else {
                r = mid
            }
        }
    }
    
    if nums[l] < nums[r] {
        return nums[l]
    }
    
    return nums[r]
}

