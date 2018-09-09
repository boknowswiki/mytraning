#!/usr/bin/python -t

import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findsum(root):
            if root == None:
                return 0

            left = findsum(root.left)
            right = findsum(root.right)
            self.maxsum = max(left+right+root.val, self.maxsum)

            ret = max(left, right) + root.val

            return ret if ret > 0 else 0


        self.maxsum = -sys.maxint -1
        findsum(root)
        return self.maxsum

