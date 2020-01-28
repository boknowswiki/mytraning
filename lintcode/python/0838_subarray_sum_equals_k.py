#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        n = len(nums)
        
        pre_sum = [0] * (n+1)
        
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
            
        #print pre_sum
            
        d = {}
        ret = 0
        
        for i in range( n+1):
            #print d
            if (pre_sum[i]-k) in d:
                ret += d[pre_sum[i]-k]
                
            d[pre_sum[i]] = d.get(pre_sum[i], 0) + 1
            
        return ret
        
