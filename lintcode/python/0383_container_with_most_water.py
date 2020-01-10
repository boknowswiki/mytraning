#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        n = len(heights)
        ret = 0
        
        left = 0
        right = n-1
        
        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[right] * (right - left)
                right -= 1
                
            ret = max(ret, area)
            
        return ret
        
        
