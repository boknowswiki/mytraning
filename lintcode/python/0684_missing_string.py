#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param str1: a given string
    @param str2: another given string
    @return: An array of missing string
    """
    def missingString(self, str1, str2):
        # Write your code here
        d = set()
        ret = []
        
        l1 = str1.split()
        l2 = str2.split()
        
        for e in l2:
            d.add(e)
            
        for e in l1:
            if e not in d:
                ret.append(e)
            
        return ret
        
        
