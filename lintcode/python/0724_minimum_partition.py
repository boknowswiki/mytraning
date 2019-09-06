#!/usr/bin/python -t

# dp solution, 01 beibao, time O(mn) space O(n)

class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def findMin(self, nums):
        # write your code here
        # dp[i] wether can reach value i
        # dp[j] |= dp[j-nums[i-1]] if j >= nums[i-1]
        # dp[0] = True
        
        n = len(nums)
        
        total = sum(nums)
        half = total/2
        dp = [False] * (half+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(half, -1, -1):
                if j >= nums[i-1]:
                    dp[j] |= dp[j-nums[i-1]]
                    
        for i in range(half, -1, -1):
            if dp[i]:
                return total - i*2
                
        return -1

