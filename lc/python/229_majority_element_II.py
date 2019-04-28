#!/usr/bin/python -t

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        if len(nums) == 0:
            return ret
        
        cnt1 = cnt2 = 0
        val1, val2 = 0, 1
        
        for i in nums:
            if cnt1 == 0 and (val2 != i):
                cnt1 = cnt1 + 1
                val1 = i
            elif (cnt2 == 0) and (val1 != i):
                cnt2 = cnt2 + 1
                val2 = i
            elif val1 == i:
                cnt1 = cnt1 + 1
            elif val2 == i:
                cnt2 = cnt2 + 1
            else:
                cnt1 = cnt1 - 1
                cnt2 = cnt2 - 1
        #print val1, val2        
        if nums.count(val1) > (len(nums)//3):
            ret.append(val1)
        if (val1 != val2) and nums.count(val2) > (len(nums)//3):
            ret.append(val2)
            
        return ret
