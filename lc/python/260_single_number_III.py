#!/usr/bin/python -t

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        b = 0
        t = 0
        for i in nums:
            t ^= i

        mask = 1
        while t & mask == 0:
            mask <<= 1

        for i in nums:
            if i & mask:
                a ^= i
            else:
                b ^= i

        return [a, b]

