#!/usr/bin/python -t

#Time O(logmn) space O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        start = 0
        end = m*n - 1
        
        while start <= end:
            mid = (start+end)/2
            val = matrix[mid/n][mid%n]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return False
