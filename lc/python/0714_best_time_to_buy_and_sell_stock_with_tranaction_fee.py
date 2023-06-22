# dp
# time O(n)
# space O(1)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0
        
        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        
        return free

# dp
# time O(n)
# space O(n)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # hold[i] is the max profit at ith day with holding a stock.
        # free[i] is the max profix at ith day without holding a stock.
        # hold[i] = max(hold[i-1], free[i-1]-prices[i])
        # free[i] = max(free[i-1], hold[i-1] + price[i]-fee)
        # hold[0] = -prices[0], free[0] = 0
        # return free[n-1]
        n = len(prices)
        hold, free = [0] * n, [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1], free[i-1]-prices[i])
            free[i] = max(free[i-1], hold[i-1]+prices[i]-fee)

        return free[n-1]
