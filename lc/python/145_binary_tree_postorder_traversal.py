#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return ret
        stack = [root]

        while stack:
            node = stack.pop()
            if not isinstance(node, TreeNode):
                ret.append(node)
                continue
            stack.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root, ret):
            if root:
                postorder(root.left, ret)
                postorder(root.right, ret)
                ret.append(root.val)
                
            return
        
        ret = []
        postorder(root, ret)
        
        return ret
