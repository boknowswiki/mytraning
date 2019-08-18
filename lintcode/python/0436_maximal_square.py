#!/usr/bin/python -t

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        # state: dp[i][j], the largest square at point [i,j]
        # function: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        # init: dp[i][j] 1 if matrix[i][j] == 1
        # result: ret*ret ret = max(ret, dp[i][j])
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for i in range(m)]
        ret = 0
            
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                    #ret = max(ret, dp[i][j])
                else:
                    if matrix[i][j] == 1:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ret = max(ret, dp[i][j])
                    
        return ret * ret

if __name__ == '__main__':
    s = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    ss = Solution()
    print "answer is %s" % ss.maxSquare(s)

