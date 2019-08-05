#!/usr/bin/python -t

# dp solution, time O(mn), space O(m)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [0] * (m+1)
        ret = 0
        
        for i in range(n):
            for j in range(m, -1, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]]+V[i])
                    ret = max(ret, dp[j])
                
        return ret

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [[0] * (m+1) for i in range(n+1)]
        
        for i in range(n):
            for j in range(1, m+1):
                dp[i+1][j] = dp[i][j]
                if j >= A[i]:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-A[i]]+V[i])
                
        return dp[n][m]

if __name__ == '__main__':
    m = 1000
    s = [19,53,61,74,98,70,15,59,64,29,98,79,74,85,52,70,84,91,84,75,78,72,5,46,26,95,38,79,28,92,12,37,37,58,94,44,25,3,12,67,2,98,12,2,34,68,68,81,92,16,63,47,96,9,32,24,15,4,97,80,76,15,69,22,85,68,70,85,71,24,64,22,13,28,76,13,93,95,70,80,43,6,36,91,17,94,21,30,69,34,39,33,18,75,36,7,15,34,89,59]
    v = [12,61,63,78,49,46,44,36,37,66,43,16,14,73,72,72,83,15,83,65,21,49,36,20,22,80,94,3,73,1,91,62,8,58,79,67,53,8,85,82,70,43,22,53,22,14,41,41,77,75,91,7,39,67,33,65,34,16,93,58,67,13,69,41,42,70,40,11,31,90,31,84,61,15,13,46,10,57,31,94,77,67,57,9,75,24,75,56,27,72,5,81,79,53,96,67,60,42,82,34]
    ss = Solution()
    print "answer is %s" % ss.backPackII(m, s, v)
