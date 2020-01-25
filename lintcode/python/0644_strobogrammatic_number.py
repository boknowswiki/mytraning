#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        n = len(num)
        d = { '0' : '0', '1' : '1', '6' : '9', '9' : '6', '8' : '8'}
        
        l = 0
        r = n-1
        
        while l <= r:
            if num[l] not in d or (d[num[l]] != num[r]):
                return False
            
            l += 1
            r -= 1
            
        return True
        
        
