#!/usr/bin/python -t

class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        # Write your code here
        n = len(bits)
        
        index = 0
        
        while index < n-1:
            if bits[index] == 0:
                index += 1
            else:
                index += 2
                
        return index == n-1
