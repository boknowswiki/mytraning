#!/usr/bin/python -t

# dp solution, wanquan beibao, time O(mn) space O(n)

class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """
    def cutting(self, prices, n):
        # Write your code here
        # dp[i] the max value at lengh i
        # dp[n]
        
        m = len(prices)
        
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i >= j:
                    dp[i] = max(dp[i], dp[i-j]+prices[j-1])
                    
        print dp
        return dp[n]

if __name__ == '__main__':
    s = [3,5,8,9,10,17,17,20]
    d = 8
    ss = Solution()
    print "answer is %s" % ss.cutting(s, d)
