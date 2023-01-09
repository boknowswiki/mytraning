#!/usr/bin/python -t

# hash map and dfs with memo
# time O(n^2*m)
# space O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        memo = dict()
        def dfs(index):
            if index == len(s):
                return True

            if index in memo:
                return memo[index]

            for word in wordDict:
                if index + len(word) <= len(s) and s[index:index+len(word)] == word:
                    memo[index] = True
                    if dfs(index+len(word)):
                        return True

            memo[index] = False
            return False
        
        return dfs(0)


"""
Time: O(N^2 * M). N is the length of the s. M is the number of word in wordDict.
Note that s[i:i+len(word)]==word takes O(N) time.

Space: O(N) for the recursion memory stack size.

dfs(i) := will return starting at index i, if i to the end the string can be separated.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i==len(s): return True
            if i in history and not history[i]: return False
            
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    history[i] = True
                    if dfs(i+len(word)): return True
            history[i] = False
            return False
        
        history = {}
        return dfs(0)
"""
For interview preparation, similar problems, check out my GitHub.
It took me a lots of time to make the solution. Becuase I want to help others like me.
Please give me a star if you like it. Means a lot to me.
https://github.com/wuduhren/leetcode-python
"""

#my dp solution
#time O(n^2) space O(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        canbreak = [False]*(n+1)
        canbreak[0] = True
        
        for i in range(n+1):
            for j in range(i):
                if canbreak[j] and s[j:i] in wordDict:
                    canbreak[i] = True
                    
        return canbreak[n]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] *(n+1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        
        for i in range(n):
            for j in range(i, n):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]


#The idea is the following:
#d is an array that contains booleans
#d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word
#Example:
#s = "leetcode"
#words = ["leet", "code"]
#d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
#d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
#The result is the last index of d.

def word_break(s, words):
    d = [False] * len(s)    
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]
