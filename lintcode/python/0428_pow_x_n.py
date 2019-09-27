#!/usr/bin/python -t

# er fen

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        
        if n < 0:
            x = 1/x
            n = -n
        ret = 1
        tmp = x
        
        while n > 0:
            if n%2 == 1:
                ret *= tmp
                
            tmp *= tmp
            n = n/2
            
        return ret

