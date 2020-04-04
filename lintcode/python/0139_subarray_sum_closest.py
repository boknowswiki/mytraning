#!/usr/bin/python -t

# subarray
# presum and sort
# time nlog(n)

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return [0, 0]
            
        pre_sum = [0] * (n+1)
        pre_list = [(0, -1)]
        
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
            pre_list.append((pre_sum[i+1], i))

        #print pre_list
        pre_list = sorted(pre_list, key=lambda x: x[0])
        #print pre_list
        
        ret = [0, 0]
        diff = sys.maxint
        
        for i in range(len(pre_list)-1):
            if abs(pre_list[i+1][0] - pre_list[i][0]) < diff:
                diff = abs(pre_list[i+1][0] - pre_list[i][0])
                ret[0] = min(pre_list[i+1][1], pre_list[i][1]) + 1
                ret[1] = max(pre_list[i+1][1], pre_list[i][1])
        
        
        
        return ret
        
