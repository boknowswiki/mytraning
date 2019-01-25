#!/usr/bin/python -t 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start = 0
        end = n - 1
        while start < end:
            s[end], s[start] = s[start], s[end]
            start = start + 1
            end = end - 1
            
        return

s[::-1] python reverse string
