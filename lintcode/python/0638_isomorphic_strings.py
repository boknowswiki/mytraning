#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        d_s = {}
        d_t = {}
        
        m = len(s)
        n = len(t)
        if m != n:
            return False
            
        for i in range(m):
            if d_s.get(s[i]) != d_t.get(t[i]):
                return False
                
            d_s[s[i]] = i+1
            d_t[t[i]] = i+1
            
        return True
        
