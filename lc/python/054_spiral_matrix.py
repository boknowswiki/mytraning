#!/usr/bin/python -t

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        ret = []
        if m == 0:
            return ret
        n = len(matrix[0])
        row = 0
        col = -1

        while True:
            #left to right
            for i in xrange(n):
                col = col + 1
                ret.append(matrix[row][col])

            m = m - 1
            if m == 0:
                break

            #top to bottom
            for i in xrange(m):
                row = row + 1
                ret.append(matrix[row][col])

            n = n - 1
            if n == 0:
                break

            #right to left
            for i in xrange(n):
                col = col - 1
                ret.append(matrix[row][col])

            m = m - 1
            if m == 0:
                break
            #bottom to top
            for i in xrange(m):
                row = row - 1
                ret.append(matrix[row][col])

            n = n - 1
            if n == 0:
                break

        return ret

