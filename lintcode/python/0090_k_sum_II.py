#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A:
            return []
            
        ret = []
        
        self.dfs(A, k, target, 0, [], ret)
        
        return ret
        
    
    def dfs(self, nums, k, target, start, path, ret):
        if target < 0 or k < 0:
            return
        
        if target == 0 and k == 0:
            ret.append(list(path))
            return
        
        for i in range(start, len(nums)):
            if target - nums[i] < 0:
                continue
            path.append(nums[i])
            self.dfs(nums, k-1, target-nums[i], i+1, path, ret)
            path.pop()
            
        return
    
    
