#!/usr/bin/python -t

# dfs 

#1可以直接到6，但是1和9之间隔着5
#由于1,3,7,9是对称的，所以我们乘4即可，然后再对数字2调用递归函数，2,4,6,9也是对称的，再乘4，最后单独对5调用一次，然后把所有的加起来就是最终结果了

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def numberOfPatterns(self, m, n):
        # Write your code here
        dp = [[0]* 10 for i in range(10)]
        
        dp[1][3] = dp[3][1] = 2
        dp[7][9] = dp[9][7] = 8
        dp[3][7] = dp[7][3] = dp[1][9] = dp[9][1] = dp[4][6] = dp[6][4] = dp[2][8] = dp[8][2] = 5
        dp[1][7] = dp[7][1] = 4
        dp[3][9] = dp[9][3] = 6
        
        v = [False] * 10
        ret = 0
        for i in range(m, n+1):
            ret += self.dfs(1, i-1, dp, v) * 4
            ret += self.dfs(2, i-1, dp, v) * 4
            ret += self.dfs(5, i-1, dp, v)
            
        return ret
        
    def dfs(self, cur, remain, dp, v):
        if remain == 0:
            return 1
        v[cur] = True
        ret = 0
        
        for i in range(1, 10):
            if not v[i] and (dp[cur][i] == 0 or v[dp[cur][i]]):
                ret += self.dfs(i, remain-1, dp, v)
                
        v[cur] = False
        
        return ret

