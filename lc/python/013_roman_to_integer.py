#!/usr/bin/python -t

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                'X': 10, 'V': 5, 'I': 1}

        n = len(s)
        prev = 0
        ret = 0
        for i in xrange(n):
            cur = d[s[i]]
            ret = ret + (cur if cur <= prev else cur - 2*prev)
            prev = cur

        return ret

