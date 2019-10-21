#!/usr/bin/python -t

# dfs, traversal way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        self.ret = []
        self.helper(root, k1, k2)
        return self.ret
        
    def helper(self, node, k1, k2):
        if node == None:
            return
        
        if node.val > k1:
            self.helper(node.left, k1, k2)
            
        if k1 <= node.val <= k2:
            self.ret.append(node.val)
            
        if node.val < k2:
            self.helper(node.right, k1, k2)
            
        return
    
