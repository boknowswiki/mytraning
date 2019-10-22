#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        h = {}
        if not nums:
            return True
            
        for num in nums:
            if num not in h:
                h[num] = True
            else:
                return True
                
        return False
        

