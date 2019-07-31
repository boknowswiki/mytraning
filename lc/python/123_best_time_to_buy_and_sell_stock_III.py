#!/usr/bin/python -t

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution

# k == 2 case, time O(n) space O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        buy1 = buy2 = sys.maxint
        sell1 = sell2 = 0
        
        for i in range(n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i]-buy1)
            buy2 = min(buy2, prices[i]-sell1)
            sell2 = max(sell2, prices[i]-buy2)
                    
        return sell2

# improve dp state, time O(kn) space O(k)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        k = 2
        dp = [0]*(k+1)
        min_dp = [prices[0]] *(k+1)
        
        for i in range(1, n):
            for t in range(1, k+1):
                min_dp[t] = min(min_dp[t], prices[i] - dp[t-1])
                dp[t] = max(dp[t], prices[i]-min_dp[t])
                    
        return dp[k]

# improve min_val version, time O(kn) space O(kn)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        k = 2
        dp = [[0]*(n) for i in range(k+1)]
        
        for t in range(1, k+1):
            min_val = prices[0]
            for i in range(1, n):
                min_val = min(min_val, prices[i] - dp[t-1][i-1])
                dp[t][i] = max(dp[t][i-1], prices[i]-min_val)
                    
        return dp[2][n-1]

# dp solution time O(kn^2), space O(kn)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        k = 2
        dp = [[0]*(n) for i in range(k+1)]
        
        for t in range(1, k+1):
            for i in range(1, n):
                min_val = prices[0]
                for j in range(1, i+1):
                    min_val = min(min_val, prices[j] - dp[t-1][j-1])
                dp[t][i] = max(dp[t][i-1], prices[i]-min_val)
                    
        return dp[2][n-1]

# dp solution
# 对于2次的题目 一定要想到从左到右和从右到左2次！！！

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        l = [0] * n
        r = [0] * n
        
        min_val = prices[0]
        
        for i in range(1, n):
            min_val = min(min_val, prices[i])
            l[i] = max(l[i-1], prices[i]-min_val)
            
        max_val = prices[n-1]
        
        for i in range(n-2, -1, -1):
            max_val = max(max_val, prices[i])
            r[i] = max(r[i+1], max_val - prices[i])
            
        profit = 0
        print l, r
        
        for i in range(n):
            profit = max(l[i]+r[i], profit)
            
        return profit

if __name__ =='__main__':
    s = [3,3,5,0,0,3,1,4]
    ss = Solution()
    print('answer is')
    print ss.maxProfit(s)
