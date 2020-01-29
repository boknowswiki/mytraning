#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        n = len(nums)
        
        ret = []
        s = set()
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                ret.append(num)
                
        for i in range(1, n+1):
            if i not in s:
                ret.append(i)
                break
            
        return ret
        
