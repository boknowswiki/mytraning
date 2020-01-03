#!/usr/bin/python -t

# two pointers
# remove duplicated more than 2

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
            
        dup = 1
        index = 0
        i = 1
        
        while i < n:
            if nums[index] == nums[i]:
                if dup < 2:
                    index += 1
                    nums[index] = nums[i]
                    dup += 1
            else:
                index += 1
                nums[index] = nums[i]
                dup = 1
                
            i += 1
            
        return index+1
        
        
