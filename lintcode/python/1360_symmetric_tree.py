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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
            
        q = deque([root])
        
        while len(q) > 0:
            n = len(q)
            level = []
            
            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append('#')
            #print level        
            if not self.is_symmetric(level):
                return False
                
        return True
        
    def is_symmetric(self, ll):
        
        l = 0
        r = len(ll)-1
        
        while l <= r:
            if ll[l] != ll[r]:
                print l, r
                return False
            l += 1
            r -= 1
            
        return True


# dfs


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
            
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if not left or not right:
            return left == right
            
        if left.val != right.val:
            return False
            
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        
        

# DFS

import collections

class Solution(object):
    def _is_symmetric(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if r and not l:
            return False
        if l.val != r.val:
            return False
        return self._is_symmetric(l.right, r.left) and \
            self._is_symmetric(l.left, r.right)

    def isSymmetric(self, root):
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)


