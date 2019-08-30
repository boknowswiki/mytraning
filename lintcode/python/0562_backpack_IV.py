#!/usr/bin/python -t

# dp solution, time O(mn) space O(m)

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        # state: dp[i][j] ways for first ith items for j size
        # function:
        # init:
        # result:
        
        n = len(nums)
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(n):
            for j in range(nums[i], target+1):
                dp[j] += dp[j-nums[i]]
                
        return dp[target]

