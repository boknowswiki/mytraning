#!/usr/bin/python -t

# inorder bst and dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def __init__(self):
        self.ret = 0
    """
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        # write your code here.
        if not root:
            return self.ret

        self.inorder(root, L, R)

        return self.ret

    def inorder(self, node, start, end):
        if not node:
            return

        self.inorder(node.left, start, end)
        if start <= node.val <= end:
            self.ret += node.val
        self.inorder(node.right, start, end)

        return


# 其实就是树的遍历。因为是BST，可以根据数的范围剪枝。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0 
        
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) 
