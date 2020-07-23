/**
 * @param n: a non-negative integer
 * @return: the total number of full staircase rows that can be formed
 */
func arrangeCoins (n int) int {
    // Write your code here
    l := 0
    r := n

    for l + 1 < r {
        mid := (l+r)/2
        total := (1+mid)*mid/2
        if total == n {
            return mid
        } else if total < n {
            l = mid
        } else {
            r = mid
        }
    }
    
    if (1+r)*r/2 <= n {
        return r
    }
    return l
}

