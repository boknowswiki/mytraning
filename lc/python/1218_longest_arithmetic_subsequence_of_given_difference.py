# dp, hash table
# time O(n)
# space O(n)

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp[i] is the max length at ith index
        # dp[arr[i]] = dp.get(arr[i]-diff, 0) + 1
        # ret = max(ret, dp[arr[i]])

        dp = dict()
        ret = 1

        for a in arr:
            before_a = dp.get(a-difference, 0)
            dp[a] = before_a + 1
            ret = max(ret, dp[a])

        return ret
