#!/usr/bin/python -t

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if m == 0:
            return -1

        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    continue
                else:
                    break
            if j == n - 1 and haystack[i+j] == needle[j]:
                return i

        return -1 
