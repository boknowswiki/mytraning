#!/usr/bin/python -t


#非常直观的一道题，主要分为两种情况：
#
#如果a是正数，我们要想尽办法让数字大，所以我们把5插入第一次遇见的比五小的数前面。
#如果a是负数，我们要想尽办法让去掉负号后的数字小，所以我们把5插入到第一次遇见的比五大的数前面。

class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """
    def InsertFive(self, a):
        # write your code here
        if a == 0:
            return 50
            
        sign = a // abs(a)
        a = abs(a)
        residual = a
        pos = 0
        while residual > 0:
            pos += 1
            residual = residual // 10
        
        while pos > 0:
            num = a // 10 ** (pos - 1) % 10
            if num < 5 and sign > 0 or num > 5 and sign < 0:
                break
            pos -= 1
            
        result = sign * (a // (10 ** pos) * (10 ** (pos + 1)) + 5 * (10 ** pos) + a % (10 ** pos))
        return result
