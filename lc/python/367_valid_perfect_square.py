#!/usr/bin/python -t

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

