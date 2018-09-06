#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


#BFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = [root]
        d = 1
        right_most = root

        while q:
            node = q.pop(0)
            if node.left == None and node.right == None:
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if node is right_most:
                d = d + 1
                right_most = node.right if node.right else node.left

        return d


#BFS
class Solution(object):
    def minDepth(self, root):
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
                if node.left == None and node.right == None:
                    return d
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            level = q

        return d

