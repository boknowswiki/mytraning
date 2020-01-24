#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        ret = {}
        
        for s in str:
            ret[s] = ret.get(s, 0) + 1
            
        return ret
        
