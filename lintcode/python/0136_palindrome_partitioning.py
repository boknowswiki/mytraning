#!/usr/bin/python -t

# dfs
# time O(2^n)

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        ret = []
        
        self.dfs(s, 0, [], ret)
        
        return ret
        
    def dfs(self, s, start, com, ret):
        if start == len(s):
            ret.append(list(com))
            return
        
        for i in range(start, len(s)):
            ss = s[start:i+1]
            
            if self.isPalindrome(ss):
                com.append(ss)
                self.dfs(s, i+1, com, ret)
                com.pop()
                
        return
    
    def isPalindrome(self, s):
        
        return s == s[::-1]
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
                
            i += 1
            j -= 1
            
        return True


