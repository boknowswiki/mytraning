#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        ret = []
        d = {}
        
        for s in strs:
            list_s = sorted(s)
            key_s = "".join(list_s)
            #print key_s
            if key_s not in d:
                d[key_s] = [s]
            else:
                d[key_s].append(s)
                
        #print d
        
        for key in d:
            if len(d[key]) > 1:
                ret.extend(d[key])
                
        return ret
        
        
