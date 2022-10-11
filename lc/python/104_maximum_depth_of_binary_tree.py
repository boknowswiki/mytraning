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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


#BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = 0
        level = [root] if root else []

        while level:
            d = d + 1
            q = []

            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level = q

        return d

