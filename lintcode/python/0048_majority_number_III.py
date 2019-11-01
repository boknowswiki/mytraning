#!/usr/bin/python -t

# linked list tag, but haspmap

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        d = {}
        max_cnt = 0
        ret = 0
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                if d[num] > max_cnt:
                    max_cnt = d[num]
                    ret = num
                    
        return ret
        
        
        
