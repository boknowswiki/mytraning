#!/usr/bin/python -t

class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        if not nums:
            return []
            
        n = len(nums)
        ret = []
        
        for i in range(n):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
            
        for i in range(n):
            if nums[i] > 0:
                ret.append(i+1)
                
        return ret
        
    def findDisappearedNumbers(self, nums):
        # write your code here
        check = 1 << len(nums)
        for n in nums:
            check |= 1<<(n-1)
            
        ret = []
        i = 1
        while check:
            if check&1==0:
                ret.append(i)
            check>>=1
            i+=1
        return ret        
