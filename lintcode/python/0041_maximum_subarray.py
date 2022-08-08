#!/usr/bin/python -t


# array
# presum
# time O(n)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        # write your code here
        pre_sum = 0
        max_sum = -sys.maxsize-1
        min_sum = 0

        for num in nums:
            pre_sum += num
            max_sum = max(max_sum, pre_sum-min_sum)
            min_sum = min(min_sum, pre_sum)

        return max_sum


# greedy
# time O(n)
# space O(1)

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
