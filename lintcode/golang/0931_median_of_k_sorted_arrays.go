/**
 * @param nums: the given k sorted arrays
 * @return: the median of the given k sorted arrays
 */

import "math"

func findMedian (nums [][]int) float64 {
    // write your code here
    var n int
    for _, num := range nums {
        if len(num) == 0 || (len(num)== 1 && num[0] == 0) {
            continue
        }
        n += len(num)
    }
    
    if n % 2 == 1 {
        return findK(nums, n/2+1)
    }
    return (findK(nums, n/2) + findK(nums, n/2+1))/2
}

func findK (nums [][]int, target int) float64 {
    start, end := getRange(nums)
    
    for start + 1 < end {
        mid := start + (end-start)/2
        cnt := getCnt(nums, mid)
        if cnt >= target {
            end = mid
        } else {
            start = mid
        }
    }
    
    if getCnt(nums, start) >= target {
        return float64(start)
    }
    return float64(end)
}

func getCnt (nums [][]int, target int) int {
    var cnt int
    
    for _, num := range nums {
        cnt += getNolarger(num, target)
    }
    return cnt
}

func getNolarger(num []int, target int) int {
    n := len(num)
    if n == 0 || (n==1 && num[0] == 0) {
        return 0
    }
    
    l := 0
    r := len(num)-1
    
    for l+1<r {
        mid := l+(r-l)/2
        if num[mid] > target {
            r = mid
        } else {
            l = mid
        }
    }
    
    if num[l] > target {
        return l
    }
    if num[r] > target {
        return r
    }
    return r+1
}

func getRange(nums [][]int) (int, int) {
    min := math.MaxInt32
    max := math.MinInt32
    
    for _, num := range nums {
        if num[0] < min {
            min = num[0]
        }
        if num[len(num)-1] > max {
            max = num[len(num)-1]
        }
    }
    return min, max
}
