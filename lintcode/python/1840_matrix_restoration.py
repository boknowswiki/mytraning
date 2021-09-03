#!/usr/bin/python -t

# prefix sum

class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here
        before = [[0]*m for _ in range(n)]

        if not after:
            return after

        before[0][0] = after[0][0]

        for i in range(1, m):
            before[0][i] = after[0][i] - after[0][i-1]

        for i in range(1, n):
            before[i][0] = after[i][0] - after[i-1][0]

        for i in range (1, n):
            for j in range (1, m):
                before[i][j] = after[i][j] - after[i-1][j] - after[i][j-1] + after[i-1][j-1]

        return before 
