#!/usr/bin/python -t

# dfs

"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        if not root:
            return 0
            
        ret, _, _ = self.dfs(root)
        
        return ret
        
    def dfs(self, node):
        if not node:
            return 0, 0, 0
            
        ret, down, up = 0, 0, 0
        
        for c in node.children:
            ret_list = self.dfs(c)
            ret = max(ret, ret_list[0])
            if c.val + 1 == node.val:
                down = max(down, ret_list[1]+1)
            if c.val - 1 == node.val:
                up = max(up, ret_list[2]+1)
            
        ret = max(down+1+up, ret)
            
        return ret, down, up
        
        
