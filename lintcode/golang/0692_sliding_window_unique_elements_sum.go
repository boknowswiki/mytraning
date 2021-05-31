//hash and sliding window


/**
 * @param nums: the given array
 * @param k: the window size
 * @return: the sum of the count of unique elements in each window
 */
func slidingWindowUniqueElementsSum (nums []int, k int) int {
    // write your code here
    n := len(nums)

    if n < k {
        k = n
    }
    d := make(map[int]int)
    ret := 0
    sumCnt := 0

    for i := 0; i < k; i++ {
        d[nums[i]]++
        if d[nums[i]] == 1 {
            sumCnt++
        }
        if d[nums[i]] == 2 {
            sumCnt--
        }
    }

    ret += sumCnt

    l, r := 0, k
    for r < n {
        d[nums[r]]++
        if d[nums[r]] == 1 {
            sumCnt++
        }
        if d[nums[r]] == 2 {
            sumCnt--
        }

        d[nums[l]]--
        if d[nums[l]] == 1 {
            sumCnt++
        }
        if d[nums[l]] == 0 {
            sumCnt--
        }
        ret += sumCnt
        r++
        l++
    }

    return ret
}


// this solution time limit exceeded

/**
 * @param nums: the given array
 * @param k: the window size
 * @return: the sum of the count of unique elements in each window
 */
func slidingWindowUniqueElementsSum (nums []int, k int) int {
    // write your code here
    n := len(nums)

    if n <= k {
        k = n
    }
    ret := 0

    for i := 0; i < n-k+1; i++ {
        subNums := nums[i:i+k]
        d := make(map[int]int)
        for _, num := range subNums {
            d[num]++
        }
        for _, v := range d {
            if v == 1 {
                ret++
            }
        }
    }

    return ret
}

