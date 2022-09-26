#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        
        l = 0
        r = x-1
        
        while l+1 < r:
            mid = l + (r-l)//2
            val = mid*mid
            if val == x:
                return mid
            elif val < x:
                l = mid
            else:
                r = mid
                
        if r * r < x:
            return r
        return l

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
