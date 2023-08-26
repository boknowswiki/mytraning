# greedy, sort
# time O(nlogn)
# space O(1)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs in ascending order based on the second element.
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        ans = 0

        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans

# dp, sort
# time O(n^2)
# space O(n)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp[i] is the max length at ith pair
        # dp[i] = dp[j-1] + 1 if p[j][1] < p[i][0]
        # dp[0] = 1
        # return ret = max(ret, dp[i])
        sorted_pairs = sorted(pairs, key=lambda p: p[0])

        n = len(sorted_pairs)
        dp = [1] * n
        ret = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if sorted_pairs[i][1] < sorted_pairs[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)

            ret = max(ret, dp[i])

        return ret


class Solution:
    def longestPairChain(self, i: int, pairs: List[List[int]], n: int, memo: List[int]) -> int:
        if memo[i] != 0:
            return memo[i]
        memo[i] = 1
        for j in range(i + 1, n):
            if pairs[i][1] < pairs[j][0]:
                memo[i] = max(memo[i], 1 + self.longestPairChain(j, pairs, n, memo))
        return memo[i]

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        memo = [0] * n

        ans = 0
        for i in range(n):
            ans = max(ans, self.longestPairChain(i, pairs, n, memo))
        return ans
