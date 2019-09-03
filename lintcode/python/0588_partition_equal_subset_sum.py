#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        # dp[i] is at number i, the sum is i or not. same means true, else false
        #等价与背包问题，能否背到总价值的一半。
        #01背包即可。
        
        n = len(nums)
        
        total = 0
        
        for num in nums:
            total += num
            
        if total % 2 == 1:
            return False
        
        total /= 2
        
        dp = [False] * (20000)
        dp[0] = True
        
        for i in range(n):
            for j in range(total, nums[i]-1, -1):
                dp[j] |= dp[j-nums[i]]
                
        return dp[total]

