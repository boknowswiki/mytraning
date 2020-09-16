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
    @param root: the binary tree of the  root
    @return: return a list of double
    """
    def averageOfLevels(self, root):
        # write your code here
        if not root:
            return []
            
        q = [root]
        ret = []
        
        while len(q) > 0:
            level = []
            cnt = len(q)
            total = 0
            for node in q:
                total += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                    
            ret.append(float(total)/cnt)
            q = level
            
        return ret
