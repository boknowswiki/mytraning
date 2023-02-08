#!/usr/bin/python -t

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i, v):
            if i == len(s):
                self.a.append(v[1:])
                return

            for w in wordDict:
                if s[i:].startswith(w):
                    dfs(i + len(w), v + ' ' + w)

        self.a = []
        dfs(0, '')
        return self.a

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]

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

