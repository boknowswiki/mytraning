#!/usr/bin/python -t

#time O(log2^n) space O(1)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        
        l = 1
        r = n
        
        while l < r:
            m = l + (r-l)/2
            
            need = (1+m)*m/2
            if need <= n:
                l = m+1
            else:
                r = m
                
        return l-1
