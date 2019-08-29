#!/usr/bin/python -t

# dp solution time O(n) space O(n)

class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
            
        dp = [0] * n
        
        # start from second house
        dp[0] = 0
        dp[1] = nums[1]
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        ret = dp[n-1]
        
        # start from first house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return max(ret, dp[n-2])

class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        # dp[i] is the maximum money can rob at until ith house
        # function dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # init: dp[i] = 0, start from dp[0] to dp[n-2] and dp[1] to dp[n-1]
        # result max(dp[i], dp[i-1])
        
        n = len(nums)
        if n == 0:
            return 0
        
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)
        
        dp1[0] = 0
        dp1[1] = nums[0]
        # rob first house, not last house
        for i in range(2, n+1):
            if i == n:
                dp1[i] = dp1[i-1]
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i-1])
        
        dp2[0] = 0
        dp2[1] = 0
        for i in range(2, n+1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i-1])
        
        return max(dp1[n], dp2[n])
