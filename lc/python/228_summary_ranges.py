#!/usr/bin/python -t

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        ret = []
        if n == 0:
            return ret
        index = 0
        i = 0
        
        while i < n:
            start = i
            end = i
            
            while end < n -1 and (nums[end]+1 == nums[end+1]):
                end = end + 1
                
            if end > start:
                s = str(nums[start]) + "->" + str(nums[end])
                #ret.append(s)
            else:
                s = str(nums[start])
            ret.append(s)
            i = end + 1
                
        return ret

