#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        n = len(names)
        d = set()
        ret = []
        
        for name in names:
            name = name.lower()
            if name not in d:
                d.add(name)
                ret.append(name)
                
        return ret
        
