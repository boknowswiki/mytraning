
package main

import (
	"fmt"
)

// two pionters

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * @param nums: an array of integers
 * @param s: An integer
 * @return: an integer representing the minimum size of subarray
 */
func minimumSize(nums []int, s int) int {
	// write your code here
	n := len(nums)
	if n == 0 {
		return -1
	}

	ret := MaxInt
	left := 0
	sum := 0
	for right := 0; right < n; right++ {
		sum += nums[right]

		for sum >= s {
			ret = min(ret, right-left+1)
			sum -= nums[left]
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

func main() {
	a := []int{2, 3, 1, 2, 4, 3}
	b := 7
	fmt.Println(minimumSize(a, b))
}



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


/**
 * @param nums: an array of integers
 * @param s: An integer
 * @return: an integer representing the minimum size of subarray
 */
func minimumSize (nums []int, s int) int {
    // write your code here
    n := len(nums)
    if n == 0 || (n == 1 && nums[0] < s){
        return -1
    }
    
    minLen := n+1
    val := 0
    l := 0
    
    for r := 0; r < n; r++ {
        val += nums[r]
        for l <= r && val >= s {
            minLen = min(minLen, r-l+1)
            val -= nums[l]
            l++
        }
    }
    if minLen == n+1 {
        return -1
    }
    
    return minLen
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
