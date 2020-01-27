#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        ret = []
        d = {}
        
        for i in range(len(B)):
            d[B[i]] = i
            
        for i in range(len(A)):
            ret.append(d[A[i]])
            
        return ret
        
