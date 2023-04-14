# dfs with memorization
# dp, dynamic programming

# time O(n^2)
# space O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = dict()

        def dfs(l, r):
            nonlocal memo, s

            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                memo[(l, r)] = dfs(l+1, r-1)+2
            else:
                memo[(l, r)] = max(dfs(l+1, r), dfs(l, r-1))

            return memo[(l, r)]

        return dfs(0, n-1)
