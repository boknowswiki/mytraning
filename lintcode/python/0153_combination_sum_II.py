#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        
        ret = []
        
        self.dfs(num, target, 0, [], ret)
        
        return ret
        
    def dfs(self, num, target, start, com, ret):
        if target < 0:
            return
        
        if target == 0:
            ret.append(list(com))
            
        for i in range(start, len(num)):
            if i != start and num[i] == num[i-1]:
                continue
            
            if target < num[i]:
                break
            com.append(num[i])
            self.dfs(num, target-num[i], i+1, com, ret)
            com.pop()
            
        return
    
    
