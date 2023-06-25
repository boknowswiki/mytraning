# dfs with memo, dp
# time O(n^2*fuel)
# space O(n*fuel)

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        memo = {}

        MOD = 10**9+7

        def helper(cur, fuel_left):
            if fuel_left < 0:
                return 0
            if (cur, fuel_left) in memo:
                return memo[(cur, fuel_left)]

            ret = 0
            if cur == finish:
                ret = 1

            for nxt in range(n):
                if nxt != cur:
                    ret = (ret + helper(nxt, fuel_left-abs(locations[cur]-locations[nxt])))%MOD

            memo[(cur, fuel_left)] = ret

            return ret

        return helper(start, fuel) 


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]

        for i in range(fuel + 1):
            dp[finish][i] = 1

        for j in range(fuel + 1):
            for i in range(n):
                for k in range(n):
                    if k == i:
                        continue
                    if abs(locations[i] - locations[k]) <= j:
                        dp[i][j] = (dp[i][j] + dp[k][j - abs(
                            locations[i] - locations[k])]) % 1000000007

        return dp[start][fuel]
