#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -sys.maxsize-1
        def helper(node):
            if not node:
                return 0
            
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            self.ret = max(left+right+node.val, self.ret)
            
            return max(left, right) + node.val
        
        helper(root)
        
        return self.ret
    

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

