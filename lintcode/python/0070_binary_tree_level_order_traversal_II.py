#!/usr/bin/python -t

# bfs, queue and tree traversal solution

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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        ret = []
        if root == None:
            return []
            
        q = deque([root])
        
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                level.append(node.val)
                #print level
            ret.append(level)
        
        ret.reverse()
        return ret

