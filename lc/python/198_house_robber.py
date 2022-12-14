#!/usr/bin/python -t

# dp

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the total at ith house
        # dp[i] = max(dp[:i-2]) + nums[i]
        # dp[0] = nums[0], dp[1] = nums[1]
        # max(dp[n-1], dp[n-2])
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[:i-1]) + nums[i]

        return max(dp[n-1], dp[n-2])

#dp solution

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+1)
        
        dp[0] = 0
        if n == 0:
            return dp[n]
        
        dp[1] = nums[0]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            
        return dp[n]

#my own solution!
#time O(n) space O(n)

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
        
        l = [0]*(n+1)
        l[0] = nums[0]
        l[1] = max(nums[0], nums[1])
        max_ret = max(l[0], l[1])
        
        for i in range(2, n):
            l[i] = max(l[i-2]+nums[i], l[i-1])
            max_ret = max(max_ret, l[i])
            
        return max_ret

#bottom-up iterator 2 variables
#time O(n) space O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        pre_1 = 0
        pre_2 = 0
        
        for i in range(n):
            pre_1, pre_2 = max(pre_1, pre_2+nums[i]), pre_1
            
        return pre_1

#bottom-up iterator with memorize
#time O(n) space O(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        l = [0]*(n+1)
        l[1] = nums[0]
        
        for i in range(1, n):
            l[i+1] = max(l[i-1]+nums[i], l[i])
            
        return l[n]

#top-down with memorize
#time O(n) space O(n)

class Solution(object):
    def __init__(self):
        self.mem = []
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def my_rob(nums, i):
            if i < 0:
                return 0
            if self.mem[i] >= 0:
                return self.mem[i]
            self.mem[i] = max(my_rob(nums, i-2)+nums[i], my_rob(nums, i-1))
            return self.mem[i]
            
        n = len(nums)
        self.mem = [-1]*(n+1)
        return my_rob(nums, n-1)

#recursive
#rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
#Time Limit Exceeded

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def my_rob(nums, i):
            if i < 0:
                return 0
            return max(my_rob(nums, i-2)+nums[i], my_rob(nums, i-1))
            
        n = len(nums)
        
        return my_rob(nums, n-1)

