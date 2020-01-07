#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        n = len(chars)
        if n < 2:
            return chars
        
        l = 0
        r = n-1
        
        while l < r:
            while l <= r and chars[l].islower():
                l += 1
            while l <= r and chars[r].isupper():
                r -= 1
                
            if l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
                
        #print chars        
        return chars
    
