package main

import "fmt"

// queue and sliding window
// time O(n), space O(k)

/**
 * @param nums: A list of integers.
 * @param k: An integer
 * @return: The maximum number inside the window at each moving.
 */
func maxSlidingWindow(nums []int, k int) []int {
	// write your code here
	n := len(nums)
	ret := make([]int, 0)
	if n == 0 && k == 0 {
		return ret
	}

	q := make([]int, 0)

	for i := 0; i < n; i++ {
		for len(q) != 0 && nums[i] >= nums[q[len(q)-1]] {
			q = q[:len(q)-1]
		}
		q = append(q, i)

		if i+1 >= k {
			ret = append(ret, nums[q[0]])
		}
		if i+1-k == q[0] {
			q = q[1:]
		}
	}

	return ret
}

func main() {
	a := []int{1, 2, 7, 7, 8}
	q := 3
	fmt.Println(maxSlidingWindow(a, q))
}
