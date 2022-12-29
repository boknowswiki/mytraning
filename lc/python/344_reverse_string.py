#!/usr/bin/python -t 

# two pointer

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n < 2:
            return
        
        l = 0
        r = n-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return

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
