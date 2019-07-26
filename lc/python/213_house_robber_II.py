#!/usr/bin/python -t

#dp solution

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        return max(self.helper(nums, 0, n-1), self.helper(nums, 1, n))
    
    def helper(self, nums, start, end):
        n = end - start
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[start]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1+start])
            
        return dp[n]

#Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.

#time O(n) space O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def myrob(nums, l, r):
            pre = cur = 0
            
            for i in range(l, r):
                tmp = max(pre+nums[i], cur)
                pre = cur
                cur = tmp
                
            return cur
        
        n = len(nums)
        if n < 2:
            return nums[0] if n != 0 else 0
        
        return max(myrob(nums, 0, n-1), myrob(nums, 1, n))
