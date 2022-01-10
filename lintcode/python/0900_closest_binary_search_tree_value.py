#!/usr/bin/python -t

# bst and dfs


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys

class Solution:
    def __init__(self):
        self.minVal = sys.maxsize
        self.minDiff = sys.maxsize
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return 0

        diff = abs(root.val - target)
        if diff < self.minDiff:
            self.minDiff = diff
            self.minVal = root.val

        if root.val < target:
            self.closestValue(root.right, target)
        if root.val > target:
            self.closestValue(root.left, target)

        return self.minVal

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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root or not target:
            return -1

        res = sys.maxsize

        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val

            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                return root.val
        return res
