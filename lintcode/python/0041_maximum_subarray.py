#!/usr/bin/python -t

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        
        if n == 0:
            return 0
        
        l_max = g_max = nums[0]
        
        for i in range(1, n):
            l_max = max(nums[i], l_max +nums[i])
            g_max = max(g_max, l_max)
            
        return g_max

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        
        if n == 0:
            return 0
        
        l_max = [0] * n
        g_max = [0] * n
        
        l_max[0] = g_max[0] = nums[0]
        
        for i in range(1, n):
            l_max[i] = max(nums[i], l_max[i-1]+nums[i])
            g_max[i] = max(g_max[i-1], l_max[i])
            
        return g_max[n-1]

if __name__ == '__main__':
    s = [-2,2,-3,4,-1,2,1,-5,3]
    ss = Solution()
    print "answer is %s" % ss.maxSubArray(s)
