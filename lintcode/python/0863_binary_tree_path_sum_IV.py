#!/usr/bin/python -t

# dfs, build mapping for level and index with val

class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """
    def pathSum(self, nums):
        # write your code here
        if not nums:
            return 0
            
        mapping = {}
        
        for num in nums:
            level = num//100
            index = (num-level*100)//10
            val = num%10
            mapping[(level,index)] = val
            
        return self.dfs(mapping, 1, 1, 0)
        
    def dfs(self, mapping, x, y, sum):
        if (x, y) not in mapping:
            return 0
            
        new_sum = sum + mapping[(x, y)]
        next_left = (x+1, 2*y-1)
        next_right = (x+1, 2*y)
        
        if next_left not in mapping and next_right not in mapping:
            return new_sum
            
        return self.dfs(mapping, x+1, 2*y-1, new_sum) + self.dfs(mapping, x+1, 2*y, new_sum)
        

