#!/usr/bin/python -t

# hash table time O(n) space O(k)

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        d = dict()
        n = len(nums)
        
        for num in nums:
            if num in d:
                d[num] += 1
            elif len(d) < k-1:
                d[num] = 1
            else:
                keys = d.keys()
                for key in keys:
                    d[key] -= 1
                    if d[key] == 0:
                        del d[key]
  
        for key in d:
            d[key] = 0
            
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] > n/k:
                    return num
                    
        return -1
        

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
        
        
        
