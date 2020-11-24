#!/usr/bin/python -t

class Solution:
    """
    @param seats: an array
    @return: the maximum distance
    """
    def maxDistToClosest(self, seats):
        # Write your code here.
        ret, left = 0, 0
        
        for right in range(len(seats)):
            if seats[right]:
                ret = max(ret, (right-left+1)/2 ) if left else right
                left = right+1
                
        return max(ret, len(seats)-left)
