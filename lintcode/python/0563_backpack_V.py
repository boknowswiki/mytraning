#!/usr/bin/python -t

# dp solution time O(mn) space O(m)

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        # dp[i] the number of possible fill the backpack at size i
        
        n = len(nums)
        
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(target, nums[i-1]-1, -1):
                dp[j] += dp[j-nums[i-1]]
            
        return dp[target]

if __name__ == '__main__':
    s = [1,2,3,3,7]
    k = 7
    ss = Solution()
    print "answer is %s" % ss.backPackV(s, k)

