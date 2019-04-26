#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            cur, val = stack.pop()
            if cur.left == None and cur.right == None:
                if val == sum:
                    return True
                
            if cur.right:
                stack.append((cur.right, val+cur.right.val))
            if cur.left:
                stack.append((cur.left, val+cur.left.val))

                
        return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
