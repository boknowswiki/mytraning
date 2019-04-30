#!/usr/bin/python -t

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, ret):
            ret.append(path)
            
            for i in range(index, len(nums)):
                dfs(nums, i+1, path+[nums[i]], ret)
                
        ret = []
        dfs(sorted(nums), 0, [], ret)
        #dfs(nums, 0, [], ret)
        
        return ret

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i >> j & 1:
                    tmp.append(nums[j])
                    
            ret.append(tmp)
            
        return ret

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        
        for num in nums:
            ret = ret + [item+[num] for item in ret]
            
        return ret
