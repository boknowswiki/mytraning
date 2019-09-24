#!/usr/bin/python -t

# binary search solution time O(nlogn) space O(n)
# both lower bound and upper bound pass the code

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        l, r = 0, n-1
        
        ret = [nums[0]]
        
        for num in nums[1:]:
            if num > ret[-1]:
                ret.append(num)
            elif num < ret[-1]:
                overwrite_index = self.lower_bound(ret, num)
                ret[overwrite_index] = num
                
        return len(ret)
        
    def lower_bound(self, nums, val):
        l,r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r)/2
            if nums[mid] < val:
                l = mid+1
            else:
                r = mid
                
        return l

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        # state: dp[i] the longest increasing subsequence number at i
        # function: dp[i] = max(dp[i], dp[j]+1) when nums[i] > nums[j]
        # init: dp[i] = 1
        #result: dp[n-1]
        n = len(nums)
        if n < 2:
            return n
            
        dp = [1] * n
        ret = dp[0] = 1
        
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                
            ret = max(ret, dp[i])
            
        return ret

