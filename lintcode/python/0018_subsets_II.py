#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        ret = []
        nums.sort()
        
        self.dfs(nums, 0, [], ret)
        
        return ret
        
    def dfs(self, nums, index, path, ret):
        ret.append(list(path))
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, ret)
            path.pop()
            
        return
    
    
