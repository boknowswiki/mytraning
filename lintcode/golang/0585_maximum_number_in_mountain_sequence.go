/**
 * @param nums: a mountain sequence which increase firstly and then decrease
 * @return: then mountain top
 */
func mountainSequence (nums []int) int {
    // write your code here
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        
        if mid == 0 && nums[mid] > nums[mid+1] {
            return nums[mid]
        }
        
        if mid == n-1 && nums[mid] > nums[mid-1] {
            return nums[mid]
        }
        
        if nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1] {
            return nums[mid]
        } else if nums[mid] > nums[mid-1] {
            l = mid
        } else {
            r = mid
        }
    }
    
    if nums[l] > nums[r] {
        return nums[l]
    }
    return nums[r]
}

