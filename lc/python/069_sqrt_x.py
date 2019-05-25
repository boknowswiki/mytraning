#!/usr/bin/python -t

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        l = 0
        r = x
        
        while l < r:
            m = l + (r-l)/2
            t = m*m
            if t == x:
                return m
            elif t > x:
                r = m
            else:
                l = m + 1
                
        return l -1
