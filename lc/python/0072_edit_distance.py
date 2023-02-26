# dp
# time O(mn)
# space O(mn)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] is the distance for ith character from word1 and jth character from word2
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if word1[i] != word2[j]
        # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]
        # init dp[i][0] = i, dp[0][j] = j
        # return dp[m][n]
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case - i steps away
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # each step has four possibilities
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # same character, i and j move ahead together
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # find min of insert, replace, remove a character
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        
        return dp[m][n]
