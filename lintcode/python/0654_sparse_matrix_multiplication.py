#!/usr/bin/python -t

# hash table

#一种时间复杂度也为 
#O(k∗n2) 的办法（k 为一行中的非零位个数）
#这种办法比较巧妙，通过初始化结果矩阵，然后把非零位逐个累乘累加的办法，而不是按照原来的矩阵乘法顺序在做。
#
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        m = len(A)
        n = len(A[0])
        l = len(B[0])
        
        ret = [[0] * l for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(l):
                        ret[i][k] += A[i][j]*B[j][k]
                        
        return ret
        
