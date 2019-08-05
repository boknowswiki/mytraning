#!/usr/bin/python -t

class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        n = len(A)
        
        dp = [[[0] * (target+1) for i in range(k+1)] for i in range(n+1)]
        
        print dp[0]
        for i in range(n+1):
            dp[i][0][0] = 1
            
        for i in range(n):
            for j in range(1, k+1):
                if j >i+1:
                    continue
                for t in range(1, target+1):
                    if A[i] <= t:
                        dp[i+1][j][t] = dp[i][j-1][t-A[i]]
                    dp[i+1][j][t] += dp[i][j][t]
                    
        return dp[n][k][target]

if __name__ == '__main__':
    s= [1,2,3,4]
    k = 2
    t = 5
    ss = Solution()
    print "answer is %s" % ss.kSum(s, k, t)
