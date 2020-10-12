#!/usr/bin/python -t

class Solution:
    """
    @param s: the string s
    @return: check if the string is interesting
    """
    def check(self, s):
        # Write your code here
        if s is None or len(s) == 0:
            return 'no'
        return 'yes' if self.dfs(s) else 'no'
    
    def dfs(self, s):
        if len(s) == 0:
            return True
        n = len(s)
        for i in range(1, n):
            prefix = s[:i]
            if prefix.isdigit():
                num = int(prefix)
                if len(s[i:]) < num:
                    continue
                suffix = s[i+num:]
                if 0 < len(suffix) < num:
                    return False
                if self.dfs(suffix):
                    return True
            else:
                break
        return False
