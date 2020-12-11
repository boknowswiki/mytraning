/**
 * @param nums: an array of integers
 * @param s: An integer
 * @return: an integer representing the minimum size of subarray
 */

const MaxInt = int((^uint(0))>>1)
func minimumSize (nums []int, s int) int {
    // write your code here
    n := len(nums)
    if n == 0 && s != 0{
        return -1
    }
    
    left := 0
    val := 0
    ret := MaxInt
    
    for right := range nums {
        val += nums[right]
        
        for left <= right && val >= s {
            ret = min(ret, right-left+1)
            val = val - nums[left]
            left++
        }
    }
    
    if ret == MaxInt {
        return -1
    }
    return ret
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
