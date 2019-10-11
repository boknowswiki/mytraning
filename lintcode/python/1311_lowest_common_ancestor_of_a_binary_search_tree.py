#!/usr/bin/python -t

# dfs, traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if root == None:
            return root
            
        father_v = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > father_v and q_val > father_v:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < father_v and q_val < father_v:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            
