#!/usr/bin/python -t

#用前缀和优化, 令 sum[i][j] = sum[0][j] + sum[1][j] + ... + sum[i][j]
#
#然后枚举上下边界, 这样就相当于在一行内, 求一个数组连续子串和为0的问题了.

# time O(n^3)

class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return None
            
        m, n = len(matrix), len(matrix[0])
        
        for top in range(m):
            pre_col = [0] * n
            for down in range(top, m):
                pre_sum = 0
                pre_hash = {0: -1}
                for col in range(n):
                    pre_col[col] += matrix[down][col]
                    pre_sum += pre_col[col]
                    if pre_sum in pre_hash:
                        return [(top, pre_hash[pre_sum]+1), (down, col)]
                    pre_hash[pre_sum] = col
                    
        return None
