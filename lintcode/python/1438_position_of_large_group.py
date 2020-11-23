#!/usr/bin/python -t

class Solution:
    """
    @param S: a string
    @return: the starting and ending positions of every large group
    """
    def largeGroupPositions(self, S):
        # Write your code here
        n = len(S)
        
        l = 0
        r = 0
        ret = []
        
        while r < n:
            while r < n and S[l] == S[r]:
                r += 1
                
            if r - l >= 3:
                ret.append([l, r-1])
                
            l = r
            
        return ret
