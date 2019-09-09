#!/usr/bin/python -t

# dp solution, zuobiao DP, time O(mn) space O(mn)

class Solution:
    """
    @param nums: 
    @return: nothing
    """
    def maxWeight(self, nums):
        # write your code here
        # dp[i][j] the maximum weighted sum path at [i, j]
        # dp[i][j] = max(dp[i-1][j], dp[i][j+1]) + nums[i][j]
        # dp[i][n] = dp[i-1][n]+nums[i][n], dp[0][j] = dp[0][j+1]+nums[0][j]
        # dp[m-1][0]
        
        if not nums or (not len(nums[0])):
            return 0
            
        m = len(nums)
        n = len(nums[0])
        
        dp = [[0] * n for i in range(n)]
        
        dp[0][n-1] = nums[0][n-1]
        
        for i in range(1, m):
            dp[i][n-1] = dp[i-1][n-1]+nums[i][n-1]
            
        for j in range(n-2, -1, -1):
            dp[0][j] = dp[0][j+1]+nums[0][j]
            
        for i in range(1, m):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(dp[i-1][j], dp[i][j+1]) + nums[i][j]
                
        return dp[m-1][0]

