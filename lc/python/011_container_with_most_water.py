#!/usr/bin/python -t

# two pointers
# time O(n)
# space O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1
        ret = 0

        while l < r:
            width = r-l
            ret = max(ret, min(height[l], height[r]) * width)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return ret

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
