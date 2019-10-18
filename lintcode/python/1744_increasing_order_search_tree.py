#!/usr/bin/python -t

# bfs, inorder traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a binary search tree
    @return: Root of a tree
    """
    def increasingBST(self, root):
        # Write your code here.
        if root == None:
            return None
            
        dummy = TreeNode(0)
        s = []
        p = dummy
        
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:    
                cur = s.pop()
                root = cur.right
                cur.left = None
                p.right = cur
                p = p.right
            
        return dummy.right
        
