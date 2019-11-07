#!/usr/bin/python -t

# bfs

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        ret = []
        s = [[i] for i in nums]
        
        while len(s) > 0:
            last = s.pop()
            
            if len(last) == len(nums):
                ret.append(last)
                
            for num in nums:
                if num not in last:
                    s.append(last+[num])
                    
        return ret
        
        

# dfs
# time O(n!*n)

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        ret = []
        
        self.dfs(nums, [], ret)
        
        return ret
        
    def dfs(self, nums, permute, ret):
        if len(permute) == len(nums):
            ret.append(list(permute))
            
        for i in range(len(nums)):
            if nums[i] not in permute:
                permute.append(nums[i])
                self.dfs(nums, permute, ret)
                permute.pop()
                
        return
    
    
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums == None:
            return []
        if nums == []:
            return [[]]
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for sub in self.permute(nums[:-1]):
                for i in xrange(len(sub)+1):
                    result += [sub[:i] + [nums[-1]] + sub[i:]]
            return result
            
            
