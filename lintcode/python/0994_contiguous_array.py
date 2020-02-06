#!/usr/bin/python -t

# hash table and presum
# like 911
# 使用一个数字sum维护到i为止1的数量与0的数量的差值。在
# loop的同时维护sum并将其插入hashmap中。
# 对于某一个sum值，若hashmap中已有这个值，则当前的i与sum上一次出现的位置之间的序列0的数量与1的数量相同。

class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        n = len(nums)
        d = {0:0}
        ret = 0
        cur_sum = 0
        
        for i in range(n):
            cur_sum += 1 if nums[i] == 1 else -1
            
            if cur_sum in d:
                ret = max(ret, i-d[cur_sum]+1)
            else:
                d[cur_sum] = i+1
                
        return ret
        
        
