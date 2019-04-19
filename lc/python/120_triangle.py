#!/usr/bin/python -t

#time O(n^2) space O(n)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        
        ret = triangle[-1]
        
        for i in xrange(n-2, -1, -1):
            for j in xrange(0, len(triangle[i])):
                ret[j] = triangle[i][j] + min(ret[j], ret[j+1])
        
        return ret[0]

