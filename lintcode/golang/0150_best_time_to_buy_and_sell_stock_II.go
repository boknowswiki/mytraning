/**
 * @param prices: Given an integer array
 * @return: Maximum profit
 */
func maxProfit (prices []int) int {
    // write your code here
    ret := 0
    n := len(prices)
    if n == 0 {
        return ret
    }
    
    for i := 1; i < n; i++ {
        diff := prices[i] - prices[i-1]
        if diff > 0 {
            ret += diff
        }
    }
    
    return ret
}

