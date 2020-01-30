#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def CountDuplicates(self, nums):
        # write your code here
        n = len(nums)
        d = {}
        ret = []
        
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0) + 1
            
            if d[nums[i]] == 2:
                ret.append(nums[i])
                
        return ret
        
