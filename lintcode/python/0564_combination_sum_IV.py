#!/usr/bin/python -t

# dp solution time O(n^2) space O(n^2)

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        # dp[i] number of possible combinations to add up to i
        # dp[i] = dp[i-A0] + dp[i-A1] + dp[i-A2]...
        # dp[0] = 1
        # dp[target]
        
        n = len(nums)
        if n == 0:
            return 0
            
        dp = [0] * (target+1)
        
        dp[0] = 1
        
        for i in range(1, target+1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]
                    
        return dp[target]

