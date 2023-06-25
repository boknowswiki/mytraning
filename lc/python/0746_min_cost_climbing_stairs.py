# dp
# time O(n)
# space O(n)
# top down

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] is the min cost from i to top
        # dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        # dp[n] = 0
        # min(dp[0], dp[1])
        n = len(cost)
        dp = [sys.maxsize]*(n+1)
        dp[n] = 0
        dp[n-1] = cost[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        
        return min(dp[0], dp[1])
