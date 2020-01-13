#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        n = len(s)
        l = 0
        r = n - 1
        
        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
                
            while l <= r and not s[r].isalnum():
                r -= 1
                
            if l <= r:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
                    
        return True
        
        
