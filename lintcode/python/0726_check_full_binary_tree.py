#!/usr/bin/python -t

# BFS

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque

class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        # write your code here
        if not root:
            return True
            
        q = deque([root])
        
        while len(q) > 0:
            l = len(q)
            
            for i in range(l):
                node = q.popleft()
                if (node.left and not node.right) or (not node.left and node.right):
                    return False
                
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                    
        return True
        

