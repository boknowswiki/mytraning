#!/usr/bin/python -t

# state: dp[i], with i the minimum coin we need
# function: dp[i] = min(dp[i], dp[i-c]+1)
# init: dp[0] = 0, for 0, we don't need any coin
# result: dp[n] == sys.maxint return -1, else dp[n]

import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxint] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
                print dp

        return -1 if dp[amount] == sys.maxint else dp[amount]

if __name__ == '__main__':
    s = [1, 2, 5]
    k = 11
    s = [2]
    k = 3
    ss = Solution()
    print('answer is %r' % ss.coinChange(s, k))
