# dp
# time O(n^2)
# space O(n^2)

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[i][diff] is the max length at ith index with diff
        # dp[right][diff] = dp[left][diff] + 1 when left < right and nums[right]-nums[left] == diff.
        # dp = {}
        # max(dp.values())
        dp = {}

        for right in range(len(nums)):
            for left in range(right):
                dp[(right, nums[right]-nums[left])] = dp.get((left, nums[right]-nums[left]), 1) + 1

        return max(dp.values())
