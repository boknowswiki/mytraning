#!/usr/bin/python -t

# 矩阵快速幂
# https://www.lintcode.com/problem/946/solution/23053?_from=collection&fromId=160

MOD = 10000007
class Matrix:
    def __init__(self,_n): # 零矩阵
        self.mat = [[0 for j in range(12)] for i in range(12)]
        self.n = _n
    def __mul__(self, m): # 矩阵乘法的计算
        tmp = Matrix(self.n)
        for i in range(self.n):
            for k in range(self.n):
                if self.mat[i][k] == 0:
                    continue
                for j in range(self.n):
                    tmp.mat[i][j] += self.mat[i][k] * m.mat[k][j]
                    tmp.mat[i][j] %= 10000007;
        return tmp
class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def calcTheValueOfAnm(self, X, m):
        n = len(X)
        if n == 0 and m==0:
            return 0;
        if m == 0:
            return X[n - 1]
        # 多开两维
        A = Matrix(n + 2)
        # 构造矩阵
        for i in range(n + 1):
            A.mat[i][0] = 10;
        for i in range(n + 2):
            A.mat[i][n + 1] = 1;
        for i in range(1,n + 1):
            for j in range(1,i + 1):
                A.mat[i][j] = 1
        # 快速幂求值
        tmp = self.qpow(A,m)
        # 根据构造矩阵得到Fn
        ans = 23 * tmp.mat[n][0] + 3 * tmp.mat[n][n + 1]
        for i in range(1,n + 1):
            ans += tmp.mat[n][i] * X[i - 1]
        return ans % MOD

    def qpow(self, A, k): # 矩阵快速幂
        B = Matrix(A.n)
        for i in range(A.n):
            B.mat[i][i] = 1 
        while k > 0:
            if k % 2 == 1:
                B = B * A
            A = A * A
            k //= 2
        return B
