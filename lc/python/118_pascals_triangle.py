#!/usr/bin/python -t

# matrix, dp
# time O(n^2)
# space O(n^2)

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        ret =[[1], [1, 1]]

        for i in range(3, numRows+1):
            level =[1] * i
            for j in range(1, i-1):
                level[j] = ret[-1][j-1] + ret[-1][j]

            ret.append(level)

        return ret

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
