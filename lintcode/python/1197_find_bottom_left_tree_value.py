#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """
    def findBottomLeftValue(self, root):
        # write your code here
        if root == None:
            return 0
            
        q = [root]
        ret = 0
        
        while len(q) != 0:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == 0:
                    ret = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return ret
