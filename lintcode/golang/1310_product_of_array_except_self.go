package main

// prefix sum array

import (
	"fmt"
)

/**
 * @param nums: an array of integers
 * @return: the product of all the elements of nums except nums[i].
 */
func productExceptSelf(nums []int) []int {
	// write your code here
	n := len(nums)
	if n == 0 {
		return nums
	}

	ret := make([]int, n)
	for i := range ret {
		ret[i] = 1
	}

	//fmt.Println(ret)

	preProduct := 1
	postProduct := 1

	for i := range nums {
		ret[i] *= preProduct
		preProduct *= nums[i]
	}

	for i := n - 1; i >= 0; i-- {
		ret[i] *= postProduct
		postProduct *= nums[i]
	}

	return ret
}

func main() {
	//b := []int{1, 2, 3, 4}
	//b := []int{0, 0, 0}
	b := []int{1, 0, 1, 1, 1, 1, 1, 1, -1, 1, 1}
	fmt.Println(productExceptSelf(b))
}
