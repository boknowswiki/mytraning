#!/usr/bin/python -t

#dp[n]=dp[n-1]+dp[n-2]+ 2*(dp[n-3]+...+d[0])
#=dp[n-1]+dp[n-2]+dp[n-3]+dp[n-3]+2*(dp[n-4]+...+d[0])
#=dp[n-1]+dp[n-3]+(dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))
#=dp[n-1]+dp[n-3]+dp[n-1]
#=2*dp[n-1]+dp[n-3]

        if N < 3:
            return N
        
        MOD = 1000000007
        
        dp = [0] * (N+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        
        for i in range(4, N+1):
            dp[i] = (2*dp[i-1]+dp[i-3]) % MOD
            
        return dp[N]



# dp solution, xulie + zhuangtai DP, time O(n) space O(n)

class Solution:
    """
    @param N: a integer
    @return: return a integer
    """
    def numTilings(self, N):
        # write your code here
        # dp[i][j] ways to fill for 2*i shape, the last shape is j
        # dp[i][0] just 2*i, no extra tile
        # dp[i][1] one more tile in the above row, means i+1 tile above, and i in current row
        # dp[i]2] one more tile in the below row, means i tile in current row, and i+1 below
        #定义状态:

        #f[i][j] 表示铺满 2 x i 的地板, 尾端形状为 j 时的方案数, 尾端一共有三种情况:

        #f[i][0] 表示尾端没有多余, 就是说一共有 2 x i 块格子
        #f[i][1] 表示上面那一行多出来了一块, 就是说上面有 i + 1 个格子, 下面有 i 个格子
        #f[i][2] 表示下面一行多出一块, 就是说上面有 i 个格子, 下面有 i + 1 个格子
        #状态转移:

        #f[i][0] = f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]  // 竖着放一块I型, 或者横着放两块I型, 或者放L型(两种方向)
        #f[i][1] = f[i - 1][0] + f[i - 1][2] // 在上面一行横着放一块I型, 或者放L型
        #f[i][2] = f[i - 1][0] + f[i - 1][1] // 在下面一行横着放一块I型, 或者放L型
        #边界: f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
        
        if N < 3:
            return N
        
        MOD = 1000000007
        
        dp = [[0, 0, 0] for i in range(N+1)]
        
        dp[0][0] = dp[1][0] = dp[1][1] = dp[1][2] = 1
        
        for i in range(1, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % MOD
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
            
        return dp[N][0]

