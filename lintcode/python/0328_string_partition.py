#!/usr/bin/python -t 

class Solution:
    """
    @param s: a string
    @return:  an array containing the length of each part
    """
    def splitString(self, s):
        # write your code here.
        n = len(s)
        m = [-1 for _ in range(26)]
        
        for i in range(n):
            m[ord(s[i])-65] = i
            
        r = 0
        ret = []
        
        while r < n:
            end = m[ord(s[r])-65]
            l = r
            
            while l < end:
                end = max(end, m[ord(s[l])-65])
                l += 1
                
            ret.append(end-r+1)
            r = end+1
            
        return ret
