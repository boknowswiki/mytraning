#!/usr/bin/python -t

# dp solution, AC time O(mnk) space O(n)

class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    def backPackVIII(self, n, value, amount):
        # write your code here
        # dp[i][j] means for first ith coins it can get j value
        # dp[i][j] = dp[i-1][j-k*value[i-1]], 0<=k<=amount[i-1]
        # dp[0][j] = False, dp[i][0] = True
        # ret += dp[m][j], 1<=j<=n
        
        m = len(value)
        
        dp = [0] *(n+1)
        dp[0] = 1
        ret = 0
        
        for i in range(m):
            cnt = [0 for x in range(n+1)]
            for j in range(value[i], n+1):
                if dp[j] == 0 and dp[j-value[i]] == 1 and cnt[j-value[i]] < amount[i]:
                    dp[j] = 1
                    ret += 1
                    cnt[j] = cnt[j-value[i]]+1
                    
        return ret
        

# dp solution, beibao, TLE, time O(mnk) space O(mn)

class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    def backPackVIII(self, n, value, amount):
        # write your code here
        # dp[i][j] means for first ith coins it can get j value
        # dp[i][j] = dp[i-1][j-k*value[i-1]], 0<=k<=amount[i-1]
        # dp[0][j] = False, dp[i][0] = True
        # ret += dp[m][j], 1<=j<=n
        
        m = len(value)
        
        dp = [[False] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(amount[i-1]+1):
                    if j >= k*value[i-1]:
                        dp[i][j] |= dp[i-1][j-k*value[i-1]]
                        if dp[i][j]:
                            break
                        
        ret = 0
        for j in range(1,n+1):
            if dp[m][j]:
                ret += 1
                
        return ret  

