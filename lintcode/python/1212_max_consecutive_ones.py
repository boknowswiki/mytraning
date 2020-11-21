#!/usr/bin/python -t

class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # Write your code here
        n = len(nums)
        ret = 0
        cnt = 0
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 0
                
        return ret
