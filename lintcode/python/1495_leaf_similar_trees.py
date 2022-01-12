#!/usr/bin/python -t

# dfs and bst inorder

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root1: the first tree
    @param root2: the second tree
    @return: returns whether the leaf sequence is the same
    """
    def leafSimilar(self, root1, root2):
        # write your code here.
        leaves1 = []
        self.inorder(root1, leaves1)
        leaves2 = []
        self.inorder(root2, leaves2)
        return leaves1 == leaves2

    def inorder(self, node, leaves):
        if not node:
            return
        if not node.left and not node.right:
            return leaves.append(node.val)

        self.inorder(node.left, leaves)
        self.inorder(node.right, leaves)
