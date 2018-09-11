#!/usr/bin/python -t

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #c = [0] * 32
        ret = 0
        n = len(nums)
        for i in xrange(32):
            c = 0
            for j in xrange(n):
                if ((nums[j] >> i) & 1):
                    c = c + 1
            ret |= ((c%3) << i)

            if ret >= 2**31:
                ret -= 2**32
        return ret



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ret = 3*sum(s) - sum(nums)
        ret = ret / 2

        return ret



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0

        for i in nums:
            two |= one & i
            one ^= i
            three = one & two
            one &= ~three
            two &= ~three

        return one


