#!/usr/bin/python -t

# bfs

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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def rightSideView(self, root):
        # write your code here
        ret = []
        if not root:
            return ret
            
        q = deque([root])
        ret.append(root.val)
        
        while len(q) > 0:
            l = len(q)
            
            level = []
            for i in range(l):
                node = q.popleft()
            
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                    
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            if level:
                ret.append(level[-1])
            
        return ret
        

