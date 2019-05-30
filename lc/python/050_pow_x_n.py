#!/usr/bin/python -t

#time O(logn) space O(logn)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            x = 1/x
            n = -n
        
        i = n/2
        mod = n%2
        
        val = self.myPow(x*x, i)
        
        if mod != 0:
            val = val * self.myPow(x, mod)

        return val

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

