/**
 * @param nums: The integer array.
 * @param target: Target to find.
 * @return: The first position of target. Position starts from 0.
 */
 
//import "fmt"

func binarySearch (nums []int, target int) int {
    // write your code here
    left := 0
    right := len(nums)-1
    
    for left + 1 < right {
       mid := (left+right)/2
       if nums[mid] >= target {
           right = mid
       } else {
           left = mid
       }
    }
    
    //fmt.Println(left, right)
    if nums[left] == target {
        return left
    }
    if nums[right] == target {
        return right
    }
    
    return -1
}

