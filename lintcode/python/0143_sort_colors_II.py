#!/usr/bin/python -t

# two pionters
# time O(nlogn) space O(1)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sortColor(colors, 1, k, 0, len(colors)-1)
        
    def sortColor(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
        
        color = (color_from+color_to)//2
        
        left = index_from
        right = index_to
        
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
                
            while left <= right and colors[right] > color:
                right -= 1
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        self.sortColor(colors, color_from, color, index_from, right)
        self.sortColor(colors, color+1, color_to, left, index_to)
        
        return
    
            
