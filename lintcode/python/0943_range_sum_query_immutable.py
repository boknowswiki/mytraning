#!/usr/bin/python -t

#better one:

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0]
        for i in nums:
            self.sum += self.sum[-1] + i,

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j + 1] - self.sum[i]

# dp solution time O(n) for init, query O(1) space O(n)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # state: dp[i] sum at ith offset
        # function: dp[i] = dp[i-1] + nums[i]
        # init: dp[i] = 0
        #result: dp[j]-dp[i] is the sum of range(i, j)
        n = len(nums)
        if n == 0:
            return
            
        self.dp = [0] * (n+1)
        
        for i in range(1, n+1):
            self.dp[i] = self.dp[i-1]+nums[i-1]
            

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

