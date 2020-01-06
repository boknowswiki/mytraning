#!/usr/bin/python -t

# two pointers


class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        n = len(s)
        if n == 0:
            return 0
            
        ret = 0
        l = 0
        r = n-1
        
        while l < r:
            if s[l] != s[r]:
                ret += abs(ord(s[l]) - ord(s[r]))
                
            l += 1
            r -= 1
            
        return ret
        
        

class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        n = len(s)
        if n == 0:
            return 0
            
        ret = 0
        l = 0
        r = n-1
        
        while l < r:
            if s[l] != s[r]:
                change = 0
                while ord(s[l]) - change != ord(s[r]):
                    #print change, ord(s[l]), ord(s[r])
                    if ord(s[l]) < ord(s[r]):
                        change -= 1
                    else:
                        change += 1
                        
                ret += abs(change)
                
            l += 1
            r -= 1
            
        return ret
        
        
