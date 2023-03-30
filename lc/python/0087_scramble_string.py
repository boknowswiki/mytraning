

# dfs with memorization

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        m ={}
        def func(s1, s2):
            if (s1, s2) in m:
                return m[(s1, s2)]
            if not sorted(s1) == sorted(s2):
                return False
            if len(s1) == 1:
                return True
            

            for i in range(1, len(s1)):
                if func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i]) or func(s1[:i], s2[:i]) and func(s1[i:], s2[i:]):
                    m[(s1, s2)] = True
                    return True
            m[(s1, s2)] = False
            return False
        return func(s1, s2)


# dp
# time O(n^4)
# space O(n^3)

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Iterate i from 0 to n-1.
            # Iterate j from 0 to n-1.
                # Set dp[1][i][j] to the boolean value of s1[i] == s2[j]. (The base case of the DP).
        # Iterate length from 2 to n.
            # Iterate i from 0 to n + 1 - length.
                # Iterate j from 0 to n + 1 - length.
                    # Iterate newLength from 1 to length - 1.
                        #If dp[newLength][i][j] && dp[length-newLength][i+newLength][j+newLength]) || (dp[newLength][i][j+l-newLength] && dp[l-newLength][i+newLength][j] is true, set dp[length][i][j] to true.
        # Return dp[n][0][0].
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)]
              for l in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for new_length in range(1, length):
                        dp1 = dp[new_length][i]
                        dp2 = dp[length-new_length][i+new_length]
                        dp[length][i][j] |= dp1[j] and dp2[j+new_length]
                        dp[length][i][j] |= dp1[j+length-new_length] and dp2[j]
        return dp[n][0][0]
