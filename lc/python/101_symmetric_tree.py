#!/usr/bin/python -t

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = []
        s.append(root)
        s.append(root)
        
        while s:
            t1 = s.pop()
            t2 = s.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            s.append(t1.left)
            s.append(t2.right)
            s.append(t1.right)
            s.append(t2.left)
            
        return True

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def issame(l, r):
            if l == None or r == None:
                return l == r
            else:
                return l.val == r.val and issame(l.left, r.right) and issame(r.left, l.right)
        
        if root == None:
            return True
        return issame(root.left, root.right)

