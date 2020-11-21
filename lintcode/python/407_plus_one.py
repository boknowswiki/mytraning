#!/usr/bin/python -t

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        n = len(digits)
        ret = []
        c = 1
        
        for i in range(n-1, -1, -1):
            num = digits[i] + c
            c = num/10
            num = num%10
            ret.insert(0, num)
            
        if c:
            ret.insert(0, c)
            
        return ret
