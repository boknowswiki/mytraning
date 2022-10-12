#!/usr/bin/python -t

# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = collections.deque([root])
        
        while q:
            cur = q.popleft()
            left = cur.left
            cur.left = cur.right
            cur.right = left
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
        return root
    

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        s = [root]
        
        while s:
            node = s.pop()
            node.left, node.right = node.right, node.left
            
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
                
        return root

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        if root == None:
            return root
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        
        return root


