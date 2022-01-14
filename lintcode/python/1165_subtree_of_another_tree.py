#!/usr/bin/python -t

# bst and dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        if not t:
            return not s
        if not s:
            return not t

        if s.val == t.val and self.isSame(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        if not s:
            return not t

        if t == None or s.val != t.val:
            return False

        return self.isSame(s.left, t.left) and self.isSubtree(s.right, t.right)
