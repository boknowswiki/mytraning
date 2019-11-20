#!/usr/bin/python -t

# dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        self.ret = []
        
        self.dfs(root)
        
        return self.ret
        
    def dfs(self, node):
        if not node:
            return -1
            
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        
        height = 1 + max(left_height, right_height)
        
        if height >= len(self.ret):
            self.ret.append([])
        
        self.ret[height].append(node.val)
        
        return height
    
            
        
