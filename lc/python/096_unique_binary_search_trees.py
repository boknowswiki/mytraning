#!/usr/bin/python -t

#time O(n^2) space O(n)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n+1)
        l[0] = 1
        l[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                l[i] += l[j-1] * l[i-j]
                
        return l[n]
