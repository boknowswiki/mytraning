#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # Write your code here
        # dp[i] the max length we got at i
        # cnt[i] the max cnt we got at i
        
        n = len(nums)
        
        #each self is one length and one cnt at beginning
        dp = [1] * n
        cnt = [1] * n
        max_len = ret = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                        
            
            if max_len == dp[i]:
                ret += cnt[i]
            if max_len < dp[i]:
                max_len = dp[i]
                ret = cnt[i]
                    
        return ret

