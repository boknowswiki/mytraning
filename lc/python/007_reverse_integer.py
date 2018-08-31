#!/usr/bin/python -t

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2**31 - 1
        sign = 1
        divden = 0
        ret = 0

        if x < 0:
            sign = -1
            x = abs(x)

        while x:
            divden = x % 10
            ret = ret * 10 + divden
            x = x / 10

        ret = ret * sign
        if ret > max_int or ret < -(max_int + 1):
            return 0
        else:
            return ret

if __name__ =='__main__':
    #s = Solution()
    #print('%s\n' % (s.longestPalindrome("babad")))
    #print('%s\n' % (s.longestPalindrome("cbbd")))
