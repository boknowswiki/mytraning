#!/usr/bin/python -t

# presum and hash table

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0

        pre_d = {0:0}
        pre_sum = 0
        ret = 0

        for i in range(n):
            pre_sum += nums[i]
            if pre_sum - k in pre_d:
                ret = max(ret, i- pre_d[pre_sum-k]+1)
            
            if pre_sum not in pre_d:
                pre_d[pre_sum] = i+1

        return ret

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        n = len(nums)
        prev_sum = 0
        d = {}
        d[0] = -1
        ret = 0
        
        for i in range(n):
            prev_sum += nums[i]
            
            if prev_sum - k in d:
                ret = max(ret, i-d[prev_sum-k])
            
            if prev_sum not in d:
                d[prev_sum] = i
                
        return ret

# presum and hash table
        
        
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        n = len(nums)
        prev_sum = [0]*(n+1)
        d = {}
        d[0] = 0
        ret = 0
        
        for i in range(1, n+1):
            prev_sum[i] = prev_sum[i-1] + nums[i-1]
            
            if prev_sum[i] - k in d:
                ret = max(ret, i-d[prev_sum[i]-k])
            
            if prev_sum[i] not in d:
                d[prev_sum[i]] = i
                
        return ret
        
        
