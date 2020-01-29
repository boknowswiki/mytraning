#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        # Write your code here
        a = set(A)
        b = set(B)
        
        ret = [0, 0, 0]
        
        ret[0] = len(a.union(b))
        ret[1] = len(a.intersection(b))
        ret[2] = len(a) - ret[1]
        
        return ret
        
        
