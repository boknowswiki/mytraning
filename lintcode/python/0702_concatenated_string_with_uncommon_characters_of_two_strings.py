#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        s_1 = set(s1)
        s_2 = set(s2)
        
        s_1, s_2 = s_1 - s_2, s_2 - s_1
        ret = ""

        for s in s1:
            if s in s_1:
                ret += s
                
        for s in s2:
            if s in s_2:
                ret += s
                
        return ret
        
        
