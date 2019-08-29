#!/usr/bin/python -t

# dp solution time O(nk) space O(k)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # dp[j] the max size can fill
        n = len(A)
        
        dp = [0] * (m+1)
        
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j], dp[j-A[i]]+A[i])
                
        print dp
                
        return dp[m]

# dp solution, space O(mn) space O(mn)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # state: dp[i][j], for i items, can it put into j size backpack
        # function: dp[i][j] = true if j >= A[i-1] and dp[i-1][j-A[i-1] is true
        # init: dp[i][j] = false and dp[0][0] = true
        # result: ret = max(ret, dp[n][i])
        
        n = len(A)
        
        dp = [[False] * (m+1) for i in range(n+1)]
        
        dp[0][0] = True
        
        for i in range(n):
            for j in range(m+1):
                dp[i+1][j] = dp[i][j]
                if j >= A[i] and dp[i][j-A[i]]:
                    dp[i+1][j] = True
                    
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i

# dp solution, time O(mn) space O(m)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        
        dp = [False] * (m+1)
        
        dp[0] = True
        ret = 0
        
        for i in range(n):
            for j in range(m, -1, -1):
                if j >= A[i] and dp[j-A[i]]:
                    dp[j] = True
                    ret = max(ret, j)
        
        return ret

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
