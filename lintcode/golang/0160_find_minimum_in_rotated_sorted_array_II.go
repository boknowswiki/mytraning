/**
 * @param nums: a rotated sorted array
 * @return: the minimum number in the array
 */
func findMin (nums []int) int {
    // write your code here
    l := 0
    r := len(nums)-1
    
    for l +1 < r {
        mid := (l+r)/2
        if nums[l] < nums[r] {
            return nums[l]
        } else if nums[l] > nums[r] {
            if nums[mid] > nums[r] {
                l = mid
            } else {
                r = mid
            }
        } else {
            l += 1
        }
    }
    
    if nums[l] < nums[r] {
        return nums[l]
    }
    
    return nums[r]
}

