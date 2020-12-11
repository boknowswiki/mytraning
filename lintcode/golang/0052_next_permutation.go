
// 从最后一个位置开始，找到一个上升点，上升点之前的无需改动。
// 然后，翻转上升点之后的降序。
// 在降序里，找到第一个比上升点大的，交换位置。

/**
 * @param nums: A list of integers
 * @return: A list of integers
 */

//import "fmt"

func nextPermutation (nums []int) []int {
    // write your code here
    n := len(nums)
    if n == 0 {
        return []int{}
    }
    
    i := n-2
    
    for i >= 0 && nums[i] >= nums[i+1] {
        i--
    }
    
    if i >= 0 {
        j := n-1
        for j > i && nums[j] <= nums[i] {
            j--
        }
        
        nums[i], nums[j] = nums[j], nums[i]
    }
    
    swap(&nums, i+1, n-1)
    
    return nums
}

func swap(nums *[]int, start int, end int){
    for start < end {
        (*nums)[start], (*nums)[end] = (*nums)[end], (*nums)[start]
        start++
        end--
    }
    return
}
