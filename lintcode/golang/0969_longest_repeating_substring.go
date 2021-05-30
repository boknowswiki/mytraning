//hash, binary search

/**
 * @param str: The input string
 * @param k: The repeated times
 * @return: The answer
 */
func longestRepeatingSubsequenceII (str string, k int) int {
    // Write your code here
    n := len(str)
    l, r := 0, n

    for l + 1 < r {
        mid := (l+r)/2
        if getLongest(str, mid) >= k {
            l = mid
        } else {
            r = mid
        }
    }

    if getLongest(str, r) >= k {
        return r
    }
    return l
}

func getLongest(str string, subLen int) int {
    d := make(map[string]int)
    maxCnt := 1
    for i := 0; i < len(str)-subLen+1; i++ {
        d[str[i:i+subLen]]++
        maxCnt = max(maxCnt, d[str[i:i+subLen]])
    }
    return maxCnt
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

