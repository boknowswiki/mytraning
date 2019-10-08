#!/usr/bin/python -t

# tree traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        if t == None:
            return ""
        
        ret = str(t.val)
        have_left = False
        
        if t.left:
            ret += "(" + self.tree2str(t.left) + ")"
            have_left = True
        if t.right:
            if not have_left:
                ret += "()"
            ret += "(" + self.tree2str(t.right) + ")"
            
        return ret
        
