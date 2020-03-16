#!/usr/bin/python -t

# two pointers
# O(n)

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        n = len(s)
        if n == 0:
            return

        offset = offset % n
        
        self.reverse(s, 0, n-1-offset)
        self.reverse(s, n-offset, n-1)
        self.reverse(s, 0, n-1)
        
        return
    
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return
    
