#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        l = 0
        r = num-1
        
        while l <= r:
            mid = l + (r-l)//2
            val = mid * mid
            if val == num:
                return True
            elif val < num:
                l = mid+1
            else:
                r = mid - 1
                
        return False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = num
        
        while l < r:
            m = l + (r-l)/2
            if m*m < num:
                l = m + 1
            else:
                r = m
                
        return True if l*l == num else False

