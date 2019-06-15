#!/usr/bin/python -t

'''

class Solution(object):
     def coinChange(self, coins, amount):
         """
         :type coins: List[int]
         :type amount: int
         :rtype: int
         """
         # Top-down dp
         if amount < 1:
             return 0
         return self.coinChange_helper(coins, amount, [0] * (amount + 1))

     def coinChange_helper(self, coins, amount, count):
         if amount < 0:
             return -1
         if amount == 0:
             return 0
         if count[amount - 1] != 0:
             return count[amount - 1]
         min_count = 2**31
         for coin in coins:
             res = self.coinChange_helper(coins, amount - coin, count)
             if res >= 0 and res < min_count:
                 min_count = 1 + res
         if min_count == 2**31:
             count[amount - 1] = -1
         else:
             count[amount - 1] = min_count
         return count[amount - 1]



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # bottom up
        #coins.sort()
        max_val = amount + 1
        d = [max_val] * (amount + 1)
        d[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    d[i] = min(d[i], d[i-coin] + 1)
                    
        return -1 if d[amount]>amount else d[amount]
'''

import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [sys.maxint] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        
        print dp
        return dp[amount] if dp[amount] <= amount else -1

if __name__ =='__main__':
    c = [1,2,5]
    ss = Solution()
    print('answer is %d' % ss.coinChange(c, 11))  
