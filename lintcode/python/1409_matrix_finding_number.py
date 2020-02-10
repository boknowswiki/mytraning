#!/usr/bin/python -t

class Solution:
    """
    @param mat: The matrix
    @return: The answer
    """
    def findingNumber(self, mat):
        # Write your code here
        n = len(mat)
        
        first_set = set(mat[0])
        
        for i in range(1, n):
            row_set = set(mat[i])
            first_set = first_set & row_set
            
        return -1 if len(first_set) == 0 else min([i for i in first_set])
        

class Solution:
    """
    @param mat: The matrix
    @return: The answer
    用map按照题意模拟即可
    """
    def findingNumber(self, mat):
        # Write your code here
        hashSet = [0 for i in range(100000 + 1)]
        n = len(mat)
        for mati in mat:
            vis = {}
            for x in mati:
                vis[x] = 1
            for key in vis:
                hashSet[key] += 1
        ans = -1
        for i in range(1, 100000 + 1):
            if hashSet[i] == n:
                ans = i
                break
        return ans
