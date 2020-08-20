/**
 * @param nums: an array containing n + 1 integers which is between 1 and n
 * @return: the duplicate one
 */
func findDuplicate (nums []int) int {
    // write your code here
    n := len(nums)
    if n == 0 || (n == 1 && nums[0] == 0) {
        return 0
    }
    
    fast := nums[nums[0]]
    slow := nums[0]
    
    for fast != slow {
        fast = nums[nums[fast]]
        slow = nums[slow]
    }
    
    slow2 := 0
    
    for slow2 != slow {
        slow2 = nums[slow2]
        slow = nums[slow]
    }
    
    return slow
}

