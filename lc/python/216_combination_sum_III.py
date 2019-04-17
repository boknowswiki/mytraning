#!/usr/bin/python -t

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(range(1,10), k, n, 0, [], ret)
        
        return ret
    
    def dfs(self, nums, k, n, start, path, ret):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ret.append(path)
            
        for i in range(start, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], ret)

