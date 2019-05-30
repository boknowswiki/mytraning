#!/usr/bin/python -t

#time O(logn) space O(1)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend > 0 and divisor > 0:
            sign = 1
        elif dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        l = 1
        r = dividend
        ret = 0
        
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ret += i
                i <<= 1
                tmp <<= 1
                
        if sign == -1:
            ret = -ret
            
        return min(max(-2147483648, ret), 2147483647)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = dividend if dividend >= 0 else -dividend
        b = divisor if divisor >= 0 else -divisor
        result = 0
        
        while a >= b:
            c = b
            i = 0
            while a >= c:
                a -= c
                result += 1<<i
                i += 1
                c <<= 1
                
        res = -result if (dividend ^ divisor) >> 31  else result
        return min(max(-2147483648, res), 2147483647)

