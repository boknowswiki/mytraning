# dp, math

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, n + 1):
            # Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i
            # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1)
            ans %= MOD
        
        return ans

# dp

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):
                # If all orders are picked and delivered then,
                # for remaining '0' orders we have only one way.
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                
                # There are some unpicked elements left. 
                # We have choice to pick any one of those orders.
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                # Number of deliveries done is less than picked orders.
                # We have choice to deliver any one of (undelivered - unpicked) orders. 
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        
        return dp[n][n]

class Solution:
    def countOrders(self, n: int) -> int:
        @functools.cache
        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                # We have completed all orders.
                return 1

            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                # We can't pick or deliver more than N items
                # Number of deliveries can't exceed number of pickups 
                # as we can only deliver after a pickup.
                return 0

            # Count all choices of picking up an order.
            ans = unpicked * totalWays(unpicked - 1, undelivered)
            ans %= MOD

            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)
            ans %= MOD

            return ans
        
        MOD = 1_000_000_007
        return totalWays(n, n)
