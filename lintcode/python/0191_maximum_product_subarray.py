#!/usr/bin/python -t

# dp solution, time O(n) space O(1)

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        # state: pre_max, prev_min
        # function, if nums[i] > 0, cur_max = (prev_max*nums[i], nums[i])
        #       global_max = max(global_max, cur_max), if nums[i]<0, switch pre_max,pre_min
        # init: pre_max = pre_min = global_max = nums[0]
        # result: global_max
        
        if len(nums) == 0:
            return 0
            
        pre_max = pre_min = global_max = nums[0]
        
        for num in nums[1:]:
            if num >= 0:
                cur_max = max(pre_max * num, num)
                cur_min = min(pre_min * num, num)
            else:
                cur_max = max(pre_min * num, num)
                cur_min = min(pre_max * num, num)
                
            pre_max = cur_max
            pre_min = cur_min
            global_max = max(global_max, cur_max)
            
        return global_max
