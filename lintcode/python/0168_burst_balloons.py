#!/usr/bin/python -t

# dp qujian
# 区间dp：在区间上进行动态规划，求解一段区间上的最优解。主要是通过合并小区间的 最优解进而得出整个大区间上最优解的dp算法。
# 题解：
# 使用算法强化班与动态规划专题班中讲的区间动态规划。
# dp[i][j] 代表 burst i+1 ~ j-1 这段时间的所有气球之后，只剩下 i,j 的最大收益。
# 
# 将原来的数组前面和后面增加两个1，最后结果就是 dp[0][n - 1]（burst 掉所有气球只剩两个1）
# i，i+1以及i+2相邻的3个构成最小的区间，然后k和j移动不断扩大更新区间，利用之前小区间的最优解更新大区间的最优解。

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        
        new_nums = [1] * (n+2)
        
        for i in range(1, n+1):
            new_nums[i] = nums[i-1]
            
        print new_nums
        n = n+2
        
        dp = [[0] * n for _ in range(n)]
        
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                dp[i][j] = 0
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+new_nums[i]*new_nums[k]*new_nums[j])
                    
        return dp[0][n-1]
        
