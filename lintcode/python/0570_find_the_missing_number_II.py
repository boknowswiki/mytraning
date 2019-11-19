#!/usr/bin/python -t

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        ret = []
        self.dfs(n, str, [], ret)
        
        return (1+n)*n/2 - sum(ret[0])
        
    def dfs(self, n, s, path, ret):
        if len(path) == n-1 and not s:
            ret.append(list(path))
            return
        
        for i in range(len(str(n))):
            if i >= len(s):
                break
            
            num = int(s[:i+1])
            # if num exists in path
            if num in path:
                continue
            
            # remove 01 cases - all other solutions would be starting with 0
            if len(s[:i+1]) != len(str(num)):
                break
           
            # remove number out of range - all other solutions are > n 
            if num > n:
                break
            
            path.append(num)
            self.dfs(n, s[i+1:], path, ret)
            path.pop()
            
        return
    
    
