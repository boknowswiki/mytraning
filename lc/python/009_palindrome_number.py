#!/usr/bin/python -t 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse_int(x):
            ret = 0
            while x:
                rest = x % 10
                ret = ret*10 + rest
                x = x/10
            return ret

        if x < 0:
            return False
        if x == reverse_int(x):
            return True
        else:
            return False

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x/div >= 10:
            div = div * 10

        while x:
            l = x/div
            r = x%10
            if l != r:
                return False
            x = (x%div)/10
            div = div / 100

        return True

if __name__ =='__main__':
    s = Solution()
    print('%r\n' % (s.isPalindrome(121)))
