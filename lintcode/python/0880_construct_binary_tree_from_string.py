#!/usr/bin/python -t

# recursion

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        if len(s) == 0:
            return None

        self.index = 0
        self.n = len(s)
        return self.dfs(s)
        
    def dfs(self, s):
        if self.index >= self.n:
            return None
        
        sign, val = 1, 0
        
        if s[self.index] == '-':
            sign = -1
            self.index += 1
            
        while self.index < self.n and s[self.index] >='0' and s[self.index] <= '9':
            val = val*10 + ord(s[self.index]) - ord('0')
            self.index += 1
        
        node = TreeNode(sign*val)
        
        if self.index >= self.n or  s[self.index] == ')':
            self.index+=1
            return node
            
        self.index+=1

        node.left = self.dfs(s)
        if self.index >= self.n or s[self.index] == ')':
            self.index+=1
            return node
        
        self.index+=1
        
        node.right = self.dfs(s)
        if self.index >= self.n or s[self.index] == ')':
            self.index+=1
            return node
            
        return node
        
