# dp
# time O(m^2)
# space O(m^2)
# top down

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        memo = {}

        def helper(op, left):
            if op == m:
                return 0

            if (op, left) in memo:
                return memo[(op, left)]

            l = nums[left]*multipliers[op] + helper(op+1, left+1)
            r = nums[n-1-(op-left)]*multipliers[op] + helper(op+1, left)

            memo[(op, left)] = max(l, r)

            return memo[(op, left)]

        return helper(0, 0)
