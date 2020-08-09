/**
 * @param nums: the array of integers
 * @param target: 
 * @return: the starting and ending position
 */
func searchRange (nums []int, target int) []int {
    // Write your code here.
    ret := []int{-1, -1}
    low := findLower(nums, target)
    high := findHigher(nums, target)
    
    ret[0] = low
    ret[1] = high
    
    return ret
}

func findLower(nums []int, target int) int {
    l := 0
    r := len(nums)-1
    
    for l + 1 < r {
        mid := (l+r)/2
        
        if nums[mid] >= target {
            r = mid
        } else {
            l = mid
        }
    }
    
    if nums[l] == target {
        return l
    }
    if nums[r] == target {
        return r
    }
    
    return -1
}

func findHigher(nums []int, target int) int {
    l := 0
    r := len(nums)-1
    
    for l+1<r {
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
