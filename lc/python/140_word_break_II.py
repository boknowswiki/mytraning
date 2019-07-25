#!/usr/bin/python -t

# dp + dfs + backtracing
#time O(n^2)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        ret = []
        
        self.dfs(s, wordDict, "", ret)
        
        return ret
    
    def dfs(self, s, wordDict, path, ret):
        if self.check(s, wordDict):
            if not s:
                ret.append(path[:-1])
                return
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, path + s[:i] + " ", ret)
                    
        
    def check(self, s, wordDict):
        n = len(s)
        
        canbreak = [False]*(n+1)
        canbreak[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if canbreak[j] and s[j:i] in wordDict:
                    canbreak[i] = True
                
        return canbreak[-1]

