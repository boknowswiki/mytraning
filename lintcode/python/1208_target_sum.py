#!/usr/bin/python -t

# dp solution, time O(nk) space O(nk)

#感觉 dp[i][j]的含义是前 i + 1个数，组合值为j时共有多少种情况
#因为既可以 + 也可以 - ，所以实际sum的范围是全正最大和的两倍
#答案把整个sum的区间往右平移了max_sum, 所以是[0, max_sum * 2 + 1],
#我把它放回0为中心的位置，即[-max_sum, max_sum + 1]，比较好理解
#
#如果第一个数为零，那么使得整个结果为0的情况有两种，nums[0]的符号为+或为-
#如果第一个数不为零，那么组合结果为nums[0]的情况只有一种，nums[0]的符号为+；
#组合结果为 -nums[0]的情况也只有一种，nums[0]的符号为-
#
#在dp的主循环中，对应每一个i, j的组合都有两种情况：+nums[i]或者-nums[i]，所以要分别累加次数。

class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        # dp[i][j] the ways for the first ith nums which the sum is j
        # dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j+nums[i-1]]
        # dp[0][0] = 1, dp[0][j] = 0 j!=0
        # ret = dp[n][s]
        
        n = len(nums)
        
        total = sum(nums)
        if total < abs(s):
            return 0
            
        d_total = 2*total
        
        dp = [[0] * (d_total+1) for i in range(n)]
        
        dp[0][0] = 1
        if nums[0] == 0:
            dp[0][total] = 2
        else:
            dp[0][total-nums[0]] = 1
            dp[0][total+nums[0]] = 1
        
        for i in range(1, n):
            for j in range(1, d_total+1):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
                if j + nums[i] <= d_total:
                    dp[i][j] += dp[i-1][j+nums[i]]
                
        return dp[n-1][s+total]


# dfs with memo, passed

class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0

        memo = {}
        
        cnt = self.dfs(nums, s, 0, memo)
        
        return cnt
        
    def dfs(self, nums, target, index, memo):
        if (index, target) in memo:
            return memo[(index, target)]
            
        if index == len(nums):
            if target == 0:
                return 1
            return 0
        cnt = 0
        
        cnt += self.dfs(nums, target-nums[index], index+1, memo)
        cnt += self.dfs(nums, target+nums[index], index+1, memo)
        memo[(index, target)] = cnt
            
        return cnt


# dfs solution, TLE

class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        self.cnt = 0
        
        self.dfs(nums, s, 0)
        
        return self.cnt
        
    def dfs(self, nums, target, index):
        if index == len(nums) and target == 0:
            self.cnt += 1
            return
        
        if index < len(nums):
            self.dfs(nums, target-nums[index], index+1)
            self.dfs(nums, target+nums[index], index+1)
            
        return

