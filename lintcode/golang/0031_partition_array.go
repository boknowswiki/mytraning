/**
 * @param nums: The integer array you should partition
 * @param k: An integer
 * @return: The index after partition
 */
func partitionArray (nums []int, k int) int {
    // write your code here
    n := len(nums)
    if n == 0  || n == 1{
        return 0
    }
    
    i := 0
    j := n-1
    
    for i <= j {
        for i <= j && nums[i] < k {
            i++
        }
        
        for i <= j && nums[j] >= k {
            j--
        }
        
        if i <= j {
            nums[i], nums[j] = nums[j], nums[i]
            i++
            j--
        }
    }
    
    return i
}

