#!/usr/bin/python -t

class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """
    def PredictTheWinner(self, nums):
        # write your code here
        # dp[i][j] is the difference that player 1 - player 2 in [i, j]
        # dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        n = len(nums)
        
        dp = [0] * (n)
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
                
        return dp[n-1] >= 0

# dp solution, qujian, time O(n^2) space O(n^2)

class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """
    def PredictTheWinner(self, nums):
        # write your code here
        # dp[i][j] the max value first player can get at [i, j]
        # dp[i][j] = max(nums[i]+min(dp[i+2][j], dp[i+1][j-1]), nums[j]+min(dp[i+1][j-1], dp[i][j-2]))
        # dp[i][i] = nums[i]
        
        n = len(nums)
        
        dp = [[0] * (n) for i in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l+i-1
                if l == 2:
                    dp[i][j] = max(dp[i][i], dp[j][j])
                else:
                    dp[i][j] = max(nums[i]+min(dp[i+2][j], dp[i+1][j-1]), nums[j] + min(dp[i+1][j-1], dp[i][j-2]))
                
        total = 0
        for num in nums:
            total += num
            
        return True if dp[0][n-1]*2 >= total else False

