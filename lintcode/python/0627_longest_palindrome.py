#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        d = {}
        
        for i in range(n):
            d[s[i]] = d.get(s[i], 0) + 1
            
        ret = 0
        add_one = 0
        
        for k in d:
            while d[k] >= 2:
                ret += 2
                d[k] -= 2
                
            if d[k] > 0:
                add_one = 1
                
        return ret + add_one
        

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        d = {}
        for c in s:
            if c in d:
                del d[c]
            else:
                d[c] = True
        
        remove = len(d)
        
        if remove > 1: 
            return len(s) - remove + 1 
        
        else:
            return len(s)
            
            
