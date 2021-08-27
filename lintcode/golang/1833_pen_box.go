package main

// dp and prefix

import (
	"fmt"
)

/**
 * @param boxes: number of pens for each box
 * @param target: the target number
 * @return: the minimum boxes
 */
func minimumBoxes(boxes []int, target int) int {
	// write your code here
	n := len(boxes)
	foundArray := make([]int, n)
	presum := make([]int, n+1)

	for i := 0; i < n; i++ {
		presum[i+1] = presum[i] + boxes[i]
	}

	left := 0
	for right := 1; right < n+1; right++ {
		for {
			if presum[right]-presum[left] <= target {
				break
			}
			left++
		}
		if presum[right]-presum[left] == target {
			foundArray[right-1] = right - left
		} else if right-1 > 0 {
			foundArray[right-1] = foundArray[right-2]
		}
	}

	ret := n + 1
	right := n
	for left := n - 1; left >= 1; left-- {
		for {
			if presum[right]-presum[left] <= target {
				break
			}
			right--
		}
		if presum[right]-presum[left] == target && foundArray[left-1] != 0 {
			ret = min(ret, foundArray[left-1]+right-left)
		}
	}
	if ret == n+1 {
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
	b := []int{1, 2, 2, 1, 1, 1}
	fmt.Println(minimumBoxes(b, 3))
}
