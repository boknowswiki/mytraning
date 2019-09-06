#!/usr/bin/python -t

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        part = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_part = self.dfs(s[i:], wordDict, memo)
            for p in sub_part:
                part.append(prefix + " " + p)
                
        if s in wordDict:
            part.append(s)
            
        memo[s] = part
        
        return part

if __name__ == '__main__':
    s = "a"
    d = []
    ss = Solution()
    print "answer is %s" % ss.wordBreak(s, d)

