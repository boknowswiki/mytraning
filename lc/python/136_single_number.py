#!/usr/bin/python -t

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        ret = 0
        for i in nums:
            ret = ret ^ i

        return ret


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        htbl = {}

        for i in nums:
            if i in htbl:
                htbl[i] = htbl[i] + 1
            else:
                htbl[i] = 1

        for i in nums:
            if htbl[i] == 1:
                return i

        return 0

