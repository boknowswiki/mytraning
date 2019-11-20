#!/usr/bin/python -t

from math import sqrt
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, num):
        res = []
        def dfs(start, n, tmp):

            for i in range(start, int(sqrt(n))+1):
                if n % i == 0:
                    dfs(i, n/i, tmp + [i])

            res.append(tmp + [n])

        dfs(2, num, [])
        res.pop()
        return res

# dfs

import math

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        ret = []
        
        self.dfs(2, n, [], ret)
        
        return ret
        
    def dfs(self, start, remain, path, ret):
        if remain == 1 and len(path) != 1:
            ret.append(list(path))
            return
        
        for i in range(start, int(math.sqrt(remain))+1):
            if remain % i == 0:
                path.append(i)
                self.dfs(i, remain/i, path, ret)
                path.pop()
        
        if remain >= start:        
            path.append(remain)
            self.dfs(remain, 1, path, ret)
            path.pop()
            
        return
    
    
