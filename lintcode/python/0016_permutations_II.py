#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        nums.sort()
        ret = []
        v = [False for _ in range(len(nums))]
        
        self.dfs(nums, v, [], ret)
        
        return ret
        
    def dfs(self, nums, v, perm, ret):
        if len(perm) == len(nums):
            ret.append(list(perm))
            return
        
        
        for i in range(len(nums)):
            if v[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not v[i-1]:
                continue
            v[i] = True
            perm.append(nums[i])
            self.dfs(nums, v, perm, ret)
            perm.pop()
            v[i] = False
            
        return
    
    
