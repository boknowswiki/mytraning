#!/usr/bin/python -t

#query time O(1), init time O(n), space O(n)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.l = [0] * (n+1)
        
        for i in range(n):
            self.l[i+1] = self.l[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.l[j+1] - self.l[i]
