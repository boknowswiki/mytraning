#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        # write your code here
        n = len(arrs)
        min_val = arrs[0][0]
        max_val = arrs[0][-1]
        ret = -sys.maxint
        
        for i in range(1, n):
            ret = min(ret, abs(arrs[i][-1]-min_val), (abs(max_val-arrs[i][0])))
            min_val = min(min_val, arrs[i][0])
            max_val = max(max_val, arrs[i][-1])
            
        return ret
        
