#!/usr/bin/python -t

# greedy
# 直接遍历一遍数组，用一个维护一个最小值以及次小值，如果当前值小于最小值则更新最小值，若大于最小值小于次小值则更新次小值，若大于次小值则返回true。


import sys

class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def increasingTriplet(self, nums):
        # write your code
        if len(nums) < 3:
            return False

        first = sys.maxsize
        second = sys.maxsize
        for num in nums:
            if num <= first:
                second = first
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
