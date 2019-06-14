#!/usr/bin/python -t

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
