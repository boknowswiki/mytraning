#!/usr/bin/python -t


import bisect

class Solution:
    """
    @param matrix: a 2D matrix
    @param k: an integer
    @return: the max sum of a rectangle in the matrix such that its sum is no larger than k
    """
    def maxSumSubmatrix(self, matrix, k):
        # Write your code here
        row, col = len(matrix), len(matrix[0])
        ret = -sys.maxint
        for i in range(col):
            rowSum = [0 for j in range(row)]
            for j in range(i, col):
                for r in range(row):
                    rowSum[r] += matrix[r][j]
                    
                curSum = 0
                curMax = -sys.maxint
                sumSet = [0]
                
                for r in range(row):
                    curSum += rowSum[r]
                    index = bisect.bisect_left(sumSet, curSum-k)
                    if index != len(sumSet):
                        curMax = max(curMax, curSum-sumSet[index])
                    bisect.insort_left(sumSet, curSum)
                    
                ret = max(ret, curMax)
                
        return ret
