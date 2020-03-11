#!/usr/bin/python -t

# dfs, better
# 时间复杂度
# 答案个数不知道, 假设为S;
# 每个答案用的时间=target;
# 所以总的时间复杂度= O(S*target), 是个NP问题

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        s = sorted(set(candidates))
        
        ret = []
        
        self.dfs(s, target, 0, [], ret)
        
        return ret
        
    def dfs(self, s, target, start, path, ret):
        if target == 0:
            ret.append(list(path))
            return
        
        for i in range(start, len(s)):
            if target < s[i]:
                return
            path.append(s[i])
            self.dfs(s, target-s[i], i, path, ret)
            path.pop()
            
        return
    

# DFS, better

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
            if target < c[i]:
                break
            combination.append(c[i])
            self.dfs(c, target-c[i], i, combination, ret)
            combination.pop()
            
        return
    
    

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
    
    
