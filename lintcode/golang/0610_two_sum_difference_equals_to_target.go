/**
 * @param nums: an array of Integer
 * @param target: an integer
 * @return: [num1, num2] (index1 < index2)
 */
func twoSum7 (nums []int, target int) []int {
    // write your code here
    res := []int{-1, -1}
    if len(nums) < 2 {
        return res
    }
    
    left := 0
    for left < len(nums)-1 {
        right := left+1
        for right < len(nums) {
            if current := nums[right]-nums[left]; current == target || current == -target {
                res[0] = nums[left]
                res[1] = nums[right]
                return res
            } else /*current != target*/ {
                right = increase(nums, right)
            }
        }
        left = increase(nums, left)
    }
    
    return res
}

func increase(nums []int, start int) int {
    var i int
    for i = start+1; i < len(nums) && nums[i] == nums[start]; i++ {}
    return i
}
