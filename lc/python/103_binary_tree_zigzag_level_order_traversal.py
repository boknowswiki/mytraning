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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        flip = False
        ret = []
        
        q = collections.deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if flip:
                ret.append(list(level[::-1]))
            else:
                ret.append(list(level))
            flip = not flip
                
        return ret

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root == None:
            return ret
        
        s = [root]
        left_to_right = 1
        
        while s:
            level = []
            for i in range(len(s)):
                node = s.pop(0)
                level.append(node.val)
                
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
                 
            ret.append(level[::left_to_right])
            left_to_right = -1 * left_to_right
             
        return ret
