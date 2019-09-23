#!/usr/bin/python -t

# binary search solution, time O(logn) space O(1)

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        if x == 1:
            return 1
            
        l = 0
        r = x
        
        while l < r:
            mid = (l+r)/2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid+1
            else:
                r = mid
                
        return l-1

