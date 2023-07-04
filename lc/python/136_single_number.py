#!/usr/bin/python -t

# array, bit manipulations
# time O(n)
# space O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0

        for num in nums:
            ret ^= num

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

