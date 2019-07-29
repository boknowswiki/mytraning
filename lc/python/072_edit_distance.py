#!/usr/bin/python -t

#dp solution
#stat: dp[i][j] means word1 at i, word2 at j, the least edit distance
# there are 3 editions, insert/replace/remove.
#function: dp[i][j] = min(dp[i-1][j](remove), dp[i-1][j-1](replace), dp[i][j-1](insert) + 1
#init: dp[i][0] = i, dp[0][j] = j
#result: dp[m][n]

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                dp[i][0] = i
                dp[0][j] = j

        print dp

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

        print dp
                    
        return dp[m][n]

if __name__ =='__main__':
    s1 = "horse"
    s2 = "ros"
    ss = Solution()
    print('answer is')
    print ss.minDistance(s1, s2)
