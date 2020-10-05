#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of integer
    @return: return a integer list
    """
    def findMode(self, root):
        # write your code here
        if not root:
            return []
            
        self.m = {}
        
        self.dfs(root)
        
        max_val = -sys.maxint-1
        ret = []
        for k in self.m:
            if self.m[k] > max_val:
                max_val = self.m[k]
                
        for k in self.m:
            if self.m[k] == max_val:
                ret.append(k)
                
        return ret
        
    def dfs(self, node):
        if node == None:
            return 0
            
        self.dfs(node.left)
        self.m[node.val] = self.m.get(node.val, 0) + 1
        self.dfs(node.right)
        
        return
