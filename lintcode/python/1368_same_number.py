#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        # Write your code here
        n = len(nums)
        
        d = {}
        
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                diff = i - d[nums[i]]
                
                if diff < k:
                    return "YES"
                d[nums[i]] = i
                
        return "NO"
        
