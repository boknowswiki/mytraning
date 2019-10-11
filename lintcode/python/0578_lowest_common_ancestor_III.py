#!/usr/bin/python -t

# LCA solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None
            
    def helper(self, node, A, B):
        if node == None:
            return False, False, None
            
        left_a, left_b, left_node = self.helper(node.left, A, B)
        right_a, right_b, right_node = self.helper(node.right, A, B)
        
        a = left_a or right_a or node == A
        b = left_b or right_b or node == B
        
        if node == A or node == B:
            return a, b, node
        
        if left_node != None and right_node != None:
            return a, b, node
        if left_node != None:
            return a, b, left_node
        if right_node != None:
            return a, b, right_node
            
        return a, b, None
     
