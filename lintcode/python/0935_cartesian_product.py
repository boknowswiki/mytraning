#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        # Write your code here
        ret = []
        
        self.dfs(setList, 0, [], ret)
        
        return ret
        
    def dfs(self, setList, dep, path, ret):
        if dep == len(setList):
            ret.append(list(path))
            return
            
        for i in setList[dep]:
            path.append(i)
            self.dfs(setList, dep+1, path, ret)
            path.pop()
            
        return
    
    
