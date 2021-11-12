#!/usr/bin/python -t

# dfs with memorization
# time O(n^2) space O(n)

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


# time limit exceeded solution, this is because no memorization, but how to do it?

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        ret = []

        self.dfs(s, wordDict, {}, 0, [], ret)

        return ret

    def dfs(self, s, d, memo, startIndex, path, ret):
        if startIndex == len(s):
            ret.append(path)
            return

        if s in memo:
            return memo[s]

        for i in range(startIndex, len(s)):
            prefix = s[startIndex:i+1]
            if prefix in d:
                if len(path) == 0:
                    newPath = prefix
                else:
                    newPath = path + " " + prefix
                self.dfs(s, d, memo, i+1, newPath, ret)
        
        return

