#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        n = len(nums)
        if n < 2:
            return
        
        red = 0
        blue = n-1
        i = 0
        
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                
                
        return
    
