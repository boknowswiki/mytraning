#!/usr/bin/python -t

# dfs, traversal and divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root, None, 0)
        
    def helper(self, node, parent, length):
        if node == None:
            return length
            
        if parent and node.val == parent.val+1:
            length += 1
        else:
            length = 1
            
        return max(length, self.helper(node.left, node, length),
                            self.helper(node.right, node, length))

