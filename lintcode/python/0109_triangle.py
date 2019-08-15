#!/usr/bin/python -t

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        if n == 0:
            return 0
        m = len(triangle[n-1])
        dp = [0]*m
        
        for j in range(m):
            dp[j] = triangle[n-1][j]
            
        print dp
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
                
        return dp[0]

if __name__ == '__main__':
    s = [[1],[2,3]]
    ss = Solution()
    print "answer is %s" % ss.minimumTotal(s)
