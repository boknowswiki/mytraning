package main

import (
	"fmt"
)

// dp
// time O(n^2), space O(n)

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

/**
 * @param nums: An integer array
 * @return: The length of LIS (longest increasing subsequence)
 */
func longestIncreasingSubsequence(nums []int) int {
	// dp[i] means the longest increasing subsequence at ith number..
	// dp[i] = dp[j]+1 if num[i] > nums[j]+1 for j from [0, i-1]
	// ret = max(ret, dp[i]) for i [0, n]

	n := len(nums)
	if n == 0 {
		return 0
	}
	dp := make([]int, n)

	for i := 0; i < n; i++ {
		dp[i] = 1
	}

	ret := 1
	for i := 1; i < n; i++ {
		for j := i - 1; j >= 0; j-- {
			if nums[i] > nums[j] {
				dp[i] = max(dp[i], dp[j]+1)
			}
			ret = max(ret, dp[i])
		}
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	a := []int{5, 4, 1, 2, 3}
	//a := []int{9, 3, 6, 2, 7}
	fmt.Println(longestIncreasingSubsequence(a))
}

// binary search time(nlogn) space(o(n))

func lengthOfLIS(nums []int) int {
    l := len(nums)
    if l < 1 {
        return 0
    }
    tmp := make([]int, l, l)
    tmp[0] = nums[0]
    index := 0
    for i := 1; i < l; i++ {
        if nums[i] < tmp[0] {
            tmp[0] = nums[i]
        } else if nums[i] > tmp[index] {
            index++
            tmp[index] = nums[i]
        } else {
            tmp[lisBinarySearch(tmp, 0, index, nums[i])] = nums[i]
        }
    }
    
    return index + 1
}

func lisBinarySearch(tmp []int, start, end, target int) int {
    for start + 1 < end {
        mid := start + (end - start) / 2
        if tmp[mid] == target {
            return mid
        }
        if tmp[mid] < target {
            start = mid
        } else {
            end = mid
        }
    }
    
    if tmp[start] >= target {
        return start
    }
    return end
}
