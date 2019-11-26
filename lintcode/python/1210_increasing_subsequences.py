#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """
    def findSubsequences(self, nums):
        # Write your code here
        ret = []
        
        self.dfs(nums, 0, [], ret)
        
        return ret
        
    def dfs(self, nums, index, path, ret):
        if index <= len(nums) and len(path) >= 2:
            ret.append(list(path))
        
        v = {}
        
        for i in range(index, len(nums)):
            if len(path) > 0 and path[-1] > nums[i]:
                continue
            if nums[i] in v:
                continue
            
            v[nums[i]] = True
            path.append(nums[i])
            self.dfs(nums, i+1, path, ret)
            path.pop()
        
        return
    
    
