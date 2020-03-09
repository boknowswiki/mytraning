#!/usr/bin/python -t

# LCA solution

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        d = {}
        
        while A != root:
            d[A] = True
            A = A.parent
            
        while B != root:
            if B in d:
                return B
            B = B.parent
            
        return root


# 将两个结点移动到相同的高度，然后同时向上移动，直到移动到相同的点

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        if not root:
            return root
            
        len_a = self.getLen(root, A)
        len_b = self.getLen(root, B)
        
        diff = abs(len_a - len_b)
        
        if diff:
            if len_a > len_b:
                while diff > 0:
                    A = A.parent
                    diff -= 1
            else:
                while diff > 0:
                    B = B.parent
                    diff -= 1
                    
        while A != B:
            A = A.parent
            B = B.parent
    
        return A
        
        
        
    def getLen(self, root, node):
        ret = 0
        
        while node != root:
            ret += 1
            node = node.parent
            
        return ret

