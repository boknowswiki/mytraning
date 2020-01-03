#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n < 2:
            return n
        
        index = 0
        
        for i in range(1, n):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
                
        return index+1
        

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n < 2:
            return n
            
        i = 1
        index = 0
        
        while i < n:
            while i < n and nums[index] == nums[i]:
                i +=1
                
            if i < n:
                index += 1
                nums[index] = nums[i]
                i += 1
            else:
                break
            
        return index+1
        
