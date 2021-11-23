
package main

// binary search O(logn)

import (
	"fmt"
)

/**
 * @param nums: a rotated sorted array
 * @return: the minimum number in the array
 */
func findMin(nums []int) int {
	// write your code here
	n := len(nums)
	l := 0
	r := n - 1

	for l+1 < r {
		mid := (l + r) / 2
		if nums[mid] > nums[l] && nums[l] > nums[r] {
			l = mid
		} else {
			r = mid
		}
	}
	return min(nums[l], nums[r])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	a := []int{4, 5, 6, 7, 0, 1, 2}
	//a := []int{1, 2, 4, 5, 6, 7, 0}
	//a := []int{0, 1, 2, 4, 5, 6, 7}
	//a := []int{1, 2, 4}
	//b := 3
	fmt.Println(findMin(a))
}



/**
 * @param nums: a rotated sorted array
 * @return: the minimum number in the array
 */
func findMin (nums []int) int {
    // write your code here
    n := len(nums)
    
    if n == 0 {
        return 0
    }
    
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        if nums[l] < nums[r] {
            return nums[l]
        } else {
            if nums[mid] > nums[l] {
                l = mid
            } else {
                r = mid
            }
        }
    }
    
    if nums[l] < nums[r] {
        return nums[l]
    }
    
    return nums[r]
}

