#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        def travelroot(root, k, s):
            if root == None:
                return False
            if (k - root.val) in s:
                return True
            s.add(root.val)
            return travelroot(root.left, k, s) or travelroot(root.right, k, s)
            
        return travelroot(root, k, s)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        l = []
        l.append(root)
        
        while(len(l) != 0):
            p = l.pop(0)
            if p != None:
                v = p.val
                if (k-v) in s:
                    return True
                s.add(v)
                l.append(p.right)
                l.append(p.left)
        return False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        l = []
        def inorder(root, l):
            if root == None:
                return
            inorder(root.left, l)
            l.append(root.val)
            inorder(root.right,l)
            
        inorder(root, l)
        
        start = 0
        end = len(l) -1
        
        while start < end:
            s = l[start] + l[end]
            if s == k:
                return True
            if s < k:
                start = start + 1
            else:
                end = end - 1
                
        return False


