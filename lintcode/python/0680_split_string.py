#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        ret = []
        
        self.dfs(s, 0, [], ret)
        
        return ret
        
    def dfs(self, s, start, path, ret):
        if start == len(s):
            ret.append(list(path))
            return
        
        for i in range(1, 3):
            if start + i <= len(s):
                path.append(s[start:i+start])
                self.dfs(s, i+start, path, ret)
                path.pop()
                    
        return
    
    
