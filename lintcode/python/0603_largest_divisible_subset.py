#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        # sort nums
        # dp[i] the number of subset at number i
        # dp[i] = max(dp[i], dp[j]+1) if nums[i]%nums[j] == 0 or nums[j]%nums[i] == 0
        # need a father[i] = previous number index
        # dp[i] = 1
        # ret need to append all the numbers
        
        n = len(nums)
        
        dp = [1] * n
        father = [-1] * n
        
        nums.sort()
        m, index = 0, -1
        
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if dp[j] + 1 >= dp[i]:
                        dp[i] = dp[j] + 1
                        father[i] = j
                        
            if dp[i] >= m:
                m = dp[i]
                index = i
                
        ret = []
        for i in range(m):
            ret.append(nums[index])
            index = father[index]
            
        return ret

