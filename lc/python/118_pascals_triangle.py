#!/usr/bin/python -t

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ret = []
        for i in range(numRows):
            ret.append([1]*(i+1))
            for j in range(1, i):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
            
        return ret
