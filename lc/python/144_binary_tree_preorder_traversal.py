#!/usr/bin/python -t

# binary tree dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        ret = []
        self.helper(root, ret)
        
        return ret
    
    def helper(self, node, ret):
        if not node:
            return
        
        ret.append(node.val)
        self.helper(node.left, ret)
        self.helper(node.right, ret)
        
        return

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return ret

#time O(n) space O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, ret):
            if root:
                ret.append(root.val)
                preorder(root.left, ret)
                preorder(root.right, ret)
                
            return
        
        ret = []

        preorder(root, ret)
        return ret
