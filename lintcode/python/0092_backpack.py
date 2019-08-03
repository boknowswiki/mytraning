#!/usr/bin/python -t

# dp solution


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[0] * (m+1) for i in range(n+1)]
        
        dp[0][0] = True
        
        print dp
        for i in range(n):
            for j in range(m+1):
                dp[i+1][j] = dp[i][j]
                if j >= A[i] and dp[i][j-A[i]]:
                    dp[i+1][j] = True
                    
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
                
        return 0

if __name__ == '__main__':
    k = 10
    s = [3,4,8,5]
    ss = Solution()
    print "answer is %s" % ss.backPack(k, s)
