#!/usr/bin/python -t

# binary search tree
# ST 里面找 in-order predecessor, 往左走的时候不记,往右走的时候记,就行了.
# https://www.techiedelight.com/find-inorder-predecessor-given-key-bst/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        pre = None
        while root:
            if root.val >= p.val:
                root = root.left
            else:
                pre = root
                root= root.right

        return pre


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        pre = None
        while root:
            #print root.val, p.val
            if root.val >= p.val:
                root = root.left
            else:
                if pre == None or root.val > pre.val:
                    pre = root
                root = root.right
                
        return pre
