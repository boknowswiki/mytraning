#!/usr/bin/python -t

# MLE

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        s = s.lower()
        lower_dict = self.initialize(dict)
        memo = {}
        ret = self.dfs(s, lower_dict, memo)
        
        return len(ret)
        
    def initialize(self, dict):
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
        return lower_dict
        
    def dfs(self, s, dict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        part = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in dict:
                continue
            sub_part = self.dfs(s[i:], dict, memo)
            for p in sub_part:
                part.append(prefix + " " + p)
                
        if s in dict:
            part.append(s)
            
        memo[s] = part
        return part


# AC

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        s = s.lower()
        max_len, lower_dict = self.initialize(dict)

        return self.dfs(s, 0, max_len, lower_dict, {})
        
        
    def initialize(self, dict):
        max_len = 0
        lower_dict = set()
        for word in dict:
            max_len = max(max_len, len(word))
            lower_dict.add(word.lower())
        return max_len, lower_dict
        
    def dfs(self, s, index, max_len, dict, memo):
        if index == len(s):
            return 1
            
        if index in memo:
            return memo[index]
            
        memo[index] = 0
        
        for i in range(index, len(s)):
            if i + 1 - index > max_len:
                break
            
            word = s[index:i+1]
            if word not in dict:
                continue
            memo[index] += self.dfs(s, i+1, max_len, dict, memo)
                
        return memo[index]

# dp solution time O(n^2) space O(n^2)

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        # dp[i][j] means ways from [i,j] can be found in the dictionary
        # dp[i][j] = dp[i][k]*dp[k+1][j] i<=k<j
        # dp[0][n-1]
        
        n = len(s)
        s = s.lower()
        new_dict = []
        for w in dict:
            new_dict.append(w.lower())
        
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] in new_dict:
                    dp[i][j] = 1
                    
                    
        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += dp[i][k]*dp[k+1][j]
                    
        return dp[0][n-1]

