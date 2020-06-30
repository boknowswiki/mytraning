#!/usr/bin/python -t

# dp
# time O(n^2)
# 九章算法强化班中讲到的记忆化搜索。
# memo 里记录了从 i,j 出发的最长上升序列的长度。

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
            
        ret = 0
        memo = {}
        
        for i in range(m):
            for j in range(n):
                ret = max(ret, self.helper(matrix, i, j, memo))
                
        return ret
        
    def helper(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
            
        ret = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if self.valid(matrix, cx, cy) and matrix[cx][cy] > matrix[x][y]:
                ret = max(ret, self.helper(matrix, cx, cy, memo)+1)
            else:
                continue
            
        memo[(x, y)] = ret
        return ret
        
    def valid(self, matrix, x, y):
        m = len(matrix)
        n = len(matrix[0])
        
        if 0 <= x < m and 0 <= y < n:
            return True
        return False


# 动态规划, 设定状态 f[i][j] 表示矩阵中坐标 (i, j) 的点开始的最长上升子序列
# 
# 状态转移方程:
# 
# int dx[4] = {0, 1, -1, 0};
# int dy[4] = {1, 0, 0, -1};
# 
# f[i][j] = max{ f[i + dx[k]][j + dy[k]] + 1 }
# 
# k = 0, 1, 2, 3, matrix[i + dx[k]][j + dy[k]] > matrix[i][j]
# 这道题目可以向四个方向走, 所以推荐使用记忆化搜索(递归)的写法.
# 
# (当然, 也可以反过来设定: f[i][j] 表示走到 (i, j) 的最长上升子序列, 相应的状态转移方程做一点点改变即可)

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestContinuousIncreasingSubsequence2(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return 0
            
        self.n = len(A)
        self.m = len(A[0])
        self.matrix = [[0] * self.m for i in xrange(self.n)]
        
        for i in xrange(self.n):
            for j in xrange(self.m):
                self.search(A, i, j)
        
        return max(max(row) for row in self.matrix)
        
    def search(self, A, x, y):
        if self.matrix[x][y] != 0:
            return self.matrix[x][y]
        
        longest = 1
        for dx, dy in self.DIRECTIONS:
            if x + dx < 0 or x + dx >= self.n:
                continue
            if y + dy < 0 or y + dy >= self.m:
                continue
            if A[x][y] >= A[x + dx][y + dy]:
                continue
            longest = max(longest, self.search(A, x + dx, y + dy) + 1)
        self.matrix[x][y] = longest
        return self.matrix[x][y]
