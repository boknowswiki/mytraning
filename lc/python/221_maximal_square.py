#!/usr/bin/python -t

#my dp solution

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0]) 
        
        dp = [[0]*n for i in range(m)]
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ret = max(ret, dp[i][j])
                    
        return ret*ret

#We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.
#dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.
#Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as
#\text{dp}(i, j) = \min \big( \text{dp}(i-1, j), \text{dp}(i-1, j-1), \text{dp}(i, j-1) \big) + 1. dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
#We also remember the size of the largest square found so far. In this way, we traverse the original matrix once and find out the required maximum size. This gives the side length of the square (say maxsqlenmaxsqlen). The required result is the area maxsqlen^2maxsqlen 
#2
# .
#In the previous approach for calculating dp of i^{th}i 
#th
#  row we are using only the previous element and the (i-1)^{th}(i−1) 
#th
#  row. Therefore, we don't need 2D dp matrix as 1D dp array will be sufficient for this.
#Initially the dp array contains all 0's. As we scan the elements of the original matrix across a row, we keep on updating the dp array as per the equation dp[j]=min(dp[j-1],dp[j],prev)dp[j]=min(dp[j−1],dp[j],prev), where prev refers to the old dp[j-1]dp[j−1]. For every row, we repeat the same process and update in the same dp array.

#time O(mn) space O(n)

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        dp = [0] *(n+1)

        max_sqlen = prev = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], min(dp[j-1], prev)) + 1
                    max_sqlen = max(max_sqlen, dp[j])
                    prev = dp[j]
                else:
                    dp[j] = 0
                    
                prev = tmp
                
        return max_sqlen * max_sqlen

#time O(mn) space O(mn)

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        dp = [0] *(m+1)
        for i in range(m+1):
            dp[i] = [0] *(n+1)
            
        max_sqlen = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1])) + 1
                    max_sqlen = max(max_sqlen, dp[i][j])
                    
        return max_sqlen * max_sqlen
