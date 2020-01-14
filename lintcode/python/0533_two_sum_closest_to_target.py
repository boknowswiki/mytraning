#!/usr/bin/python -t

# two pointers
# time O(nlogn) space O(1)

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        n = len(nums)
        nums.sort()
        
        l = 0
        r = n-1
        ret = sys.maxint
        
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                return 0
            elif val < target:
                l += 1
            else:
                r -= 1
            
            ret = min(ret, abs(target-val))
            
        return ret
        
