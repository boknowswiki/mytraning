#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param nums: an array
    @return: whether you could make one square using all the matchsticks the little match girl has
    """
    def makesquare(self, nums):
        # Write your code here
        if len(nums) < 4:
            return False
            
        total = sum(nums)
        if total % 4 != 0:
            return False
            
        nums.sort(reverse=True)
        target = [total/4] * 4
        
        return self.dfs(nums, 0, target)
        
    def dfs(self, nums, index, target):
        if index == len(nums):
            return True
            
        for i in range(4):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if self.dfs(nums, index+1, target):
                    return True
                target[i] += nums[index]
                
        return False
        
        

# dfs better

class Solution:
    """
    @param nums: an array
    @return: whether you could make one square using all the matchsticks the little match girl has
    """
    def makesquare(self, nums):
        # Write your code here
        if len(nums) < 4:
            return False
        tot = sum(nums)
        if tot % 4 != 0:
            return False
        target = tot / 4
        visited = set()
        def dfs(idx, k, tmp):
            if k == 1 and tmp == target:
                return True
            if tmp == target:
                return dfs(0, k - 1, 0)
            for i in range(idx, len(nums)):
                if i not in visited and tmp + nums[i] <= target:
                    visited.add(i)
                    if dfs(i + 1, k, tmp + nums[i]):
                        return True
                    visited.remove(i)
            return False
        return dfs(0, 4, 0)
        

