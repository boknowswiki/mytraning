#!/usr/bin/python -t

# one queue with BFS

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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        q = deque([root])
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(level)
            
        return ret


# DFS solution


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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        q = deque([root])
        target_level = 0
        
        while True:
            level = []
            self.dfs(root, 0, target_level, level)
            if not level:
                break
            
            ret.append(level)
            target_level += 1
            
        return ret
        
    def dfs(self, root, cur_level, target_level, level):
        if root == None or cur_level > target_level:
            return
        
        if cur_level == target_level:
            level.append(root.val)
            
        self.dfs(root.left, cur_level+1, target_level, level)
        self.dfs(root.right, cur_level+1, target_level, level)
