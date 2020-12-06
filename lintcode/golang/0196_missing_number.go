/**
 * @param nums: An array of integers
 * @return: An integer
 */
func findMissing (nums []int) int {
    // write your code here
    for i := range nums {
        for nums[i] >= 0 && nums[i] < len(nums) && nums[i] != i {
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        }
    }
    
    for i := range nums {
        if nums[i] != i {
            return i
        }
    }
    
    return len(nums)
}

