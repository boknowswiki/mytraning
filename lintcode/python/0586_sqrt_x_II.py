#!/usr/bin/python -t

# binary search, similar to 0141

class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if x >= 1:
            l, r = 1, x
        else:
            l, r = x, 1
            
        while l < r-(1e-10):
            mid = (l+r)/2
            if mid*mid < x:
                l = mid
            else:
                r = mid
                
        return l

