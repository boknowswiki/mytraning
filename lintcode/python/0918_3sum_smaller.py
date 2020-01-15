#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        nums.sort()
        n = len(nums)
        ret = 0
        
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                val = nums[i]+nums[j]+nums[k]
                if val < target:
                    ret += k-j
                    j += 1
                else:
                    k -= 1
                    
        return ret
        
        
