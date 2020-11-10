#!/usr/bin/python -t

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        self.ret = []
        self.dfs(n, k, 1, 0, [])
        
        return self.ret
        
    def dfs(self, n, k, index, cnt, path):
        if cnt == k:
            self.ret.append(list(path))
            return
        
        for i in range(index, n+1):
            if i not in path:
                path.append(i)
                self.dfs(n, k, i+1, cnt+1, path)
                path.pop()
                
        return
            
