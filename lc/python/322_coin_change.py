#!/usr/bin/python -t

# bfs
# time O(mn)
# space O(mn)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        q = collections.deque([0])
        v = set()
        v.add(0)
        cnt = 0
        
        while q:
            cnt += 1
            
            for _ in range(len(q)):
                val = q.popleft()
                for coin in coins:
                    if val + coin == amount:
                        return cnt
                    elif val + coin > amount:
                        continue
                    elif val + coin not in v:
                        v.add(val+coin)
                        q.append(val+coin)
                        
        return -1

# dp solution time O(mn), space O(n)

# state: dp[i], with i the minimum coin we need
# function: dp[i] = min(dp[i], dp[i-c]+1)                           
# init: dp[0] = 0, for 0, we don't need any coin
# result: dp[n] == sys.maxint return -1, else dp[n]

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxint]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
                    
        return -1 if dp[amount] == sys.maxint else dp[amount]

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
