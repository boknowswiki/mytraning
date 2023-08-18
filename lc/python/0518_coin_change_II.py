# dp
# top down
# time O(n*amount)
# space O(n*amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1]*(amount+1) for _ in range(n)]

        def dfs(i, target):
            nonlocal memo, n
            if target == 0:
                return 1

            if i == n:
                return 0

            if memo[i][target] != -1:
                return memo[i][target]

            if coins[i] > target:
                memo[i][target] = dfs(i+1, target)
            else:
                memo[i][target] = dfs(i, target-coins[i]) + dfs(i+1, target)

            return memo[i][target]

        return dfs(0, amount)

  # dp
  # bottom up
# time O(n*amount)
# space O(n*amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                if coins[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]

        return dp[0][amount]
