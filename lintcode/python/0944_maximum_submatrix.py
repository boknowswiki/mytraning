#!/usr/bin/python -t

# two pointers
#枚举子矩阵的上下边界 up & down, 然后将这之间的数压缩为一个一维数组（降维攻击），剩下的任务就是一维数组如何求 Maximum Subarray 了。

class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
            
        m = len(matrix)
        n = len(matrix[0])
        
        ret = 0
        
        for i in range(m):
            row = [0 for _ in range(n)]
            for j in range(i, m):
                for k in range(n):
                    row[k] += matrix[j][k]
                tmp = self.row_max(row)
                ret = max(ret, tmp)
                
        return ret
        
    def row_max(self, row):
        sum_val = 0
        ret = 0
        
        for i in range(len(row)):
            sum_val += row[i]
            ret = max(ret, sum_val)
            sum_val = max(sum_val, 0)
            
        return ret
        
