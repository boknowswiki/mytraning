#!/usr/bin/python -t

#Intuition
#
#There is a clear recursion available: the final cost f[i] to climb the staircase from some step i is f[i] = cost[i] + min(f[i+1], f[i+2]). This motivates dynamic programming.
#
#Algorithm
#
#Let's evaluate f backwards in order. That way, when we are deciding what f[i] will be, we've already figured out f[i+1] and f[i+2].
#
#We can do even better than that. At the i-th step, let f1, f2 be the old value of f[i+1], f[i+2], and update them to be the new values f[i], f[i+1]. We keep these updated as we iterate through i backwards. At the end, we want min(f1, f2).

#time O(n) space O(1)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
            
        return min(f1, f2)

#time O(n) space O(n)

'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        l = [0] * (n+1)
        
        for i in range(2, n+1):
            l[i] = min(l[i-1]+cost[i-1], l[i-2]+cost[i-2])
            
        return l[n]
'''

# dp from top to bottom

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        dp = [0] * (n+2)
        
        for i in range(n-1, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
            
        return min(dp[0],dp[1])

# dp from bottom to top
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
            
        return dp[n]

if __name__ =='__main__':
    #s = [10, 15, 20]
    s = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ss = Solution()
    print('answer is %d' % ss.minCostClimbingStairs(s))
