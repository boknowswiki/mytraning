#!/usr/bin/python -t

# string
# time O(mn), space O(1)
# another way is  KMP Algorithm

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        m = len(source)
        n = len(target)
        
        if n > m:
            return -1
            
        for i in range(m-n+1):
            offset = 0
            while offset < n and source[i+offset] == target[offset]:
                offset += 1
                #print offset
                
            if offset == n:
                return i
                
        return -1
            
