#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        start = 0;
        end = n - 1
        max_val = 0
        
        while start < end:
            max_val = max(max_val, min(height[start], height[end]) * (end-start))
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
                
        return max_val
