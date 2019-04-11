#!/usr/bin/python -t

#Time O(n) space O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        cnt = 1
        major = nums[0]
        
        for i in range(1, n):
            if nums[i] == major:
                cnt = cnt + 1
            elif cnt > 0:
                cnt = cnt - 1
            else:
                major = nums[i]
                cnt = 1
                
        return major

