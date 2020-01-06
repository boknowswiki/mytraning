#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param S: Customary string
    @return: Reversed string
    """
    def ReverseOnlyLetters(self, S):
        # write your code here
        n = len(S)
        if n < 2:
            return S
            
        left = 0
        right = n-1
        
        while left < right:
            if not ( ord('A') <= ord(S[left]) <= ord('Z') or ord('a') <= ord(S[left]) <= ord('z')):
                left += 1
                continue
            
            #print left, right    
            if not ( ord('A') <= ord(S[right]) <= ord('Z') or ord('a') <= ord(S[right]) <= ord('z')):
                right -= 1
                continue
            
            S = S[:left] + S[right] + S[left+1:right] + S[left] + S[right+1:]
            left += 1
            right -= 1
            
        return S
        
