//should correct, but no ac.

/**
 * @param prices: Given an integer array
 * @return: Maximum profit
 */

const MaxUint = ^uint(0) 
const MinUint = 0 
const MaxInt = int(MaxUint >> 1) 
const MinInt = -MaxInt - 1

func maxProfit (prices []int) int {
    // write your code here
    if len(prices) == 0 {
        return 0
    }
    
    ret := 0
    curMin := prices[0]
    
    for index := range prices {
        ret = max(ret, (prices[index] - curMin))
        
        if prices[index] < curMin {
            curMin = prices[index]
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
