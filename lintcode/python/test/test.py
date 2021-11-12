#!/usr/bin/python -t

class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        # dp[i] can break into word at ith place.
        n = len(s)
        if len(wordSet) == 0:
            return n == 0

        mem = [None]*n
        return self.dfs(s, 0, wordSet, mem)

    def dfs(self, s, startIndex, wordSet, mem):
        if startIndex == len(s):
            return True
        if mem[startIndex] != None:
            return mem[startIndex]

        for i in range(startIndex, len(s)):
            if s[startIndex:i+1] in wordSet and self.dfs(s, i+1, wordSet, mem):
                mem[startIndex] = True
                return True
            
        mem[startIndex] = False
        return False




if __name__ == '__main__':
    s = Solution()
    a = "lintcode"
    d = ["lint", "code"]
    print(s.wordBreak(a, d))