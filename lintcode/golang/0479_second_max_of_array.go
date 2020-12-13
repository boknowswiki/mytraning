/**
 * @param nums: An integer array
 * @return: The second max number in the array.
 */

const MaxInt = int((^uint(0))>>1)
const MinInt = -MaxInt-1

func secondMax (nums []int) int {
    // write your code here
    fstMax := -MaxInt-1
    sedMax := -MaxInt-1
    
    for i := range nums {
        if fstMax == MinInt || nums[i] > fstMax {
            sedMax = fstMax
            fstMax = nums[i]
        } else if sedMax == MinInt || nums[i] > sedMax {
            sedMax = nums[i]
        }
    }
    
    return sedMax
}

