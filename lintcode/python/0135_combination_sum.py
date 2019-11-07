#!/usr/bin/python -t

# DFS

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        c = sorted(set(candidates))
        ret = []
        self.dfs(c, target, 0, [], ret)
        
        return ret
        
    def dfs(self, c, target, start, combination, ret):
        if target < 0:
            return
        
        if target == 0:
            ret.append(list(combination))
            
        for i in range(start, len(c)):
            combination.append(c[i])
            self.dfs(c, target-c[i], i, combination, ret)
            combination.pop()
            
        return
    
    
