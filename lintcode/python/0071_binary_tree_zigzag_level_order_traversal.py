#!/usr/bin/python -t

# bfs, traversal way

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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        s = deque()
        s.append(root)
        cnt = 0
        
        while s:
            level = []
            q_len = len(s)
            
            for i in range(q_len):
                node = s.popleft()
                level.append(node.val)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
                    
            if cnt %2 != 0:
                ret.append(level[::-1])
            else:
                ret.append(level)
                
            cnt += 1
                
        return ret
        


# dfs, level traversal way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        self.ret = []
        self.preorder(root, 0, self.ret)
        
        return self.ret
        
    def preorder(self, node, level, ret):
        if node == None:
            return
        
        if len(ret) < level+1:
            ret.append([])
        if level %2 == 0:
            ret[level].append(node.val)
        else:
            ret[level].insert(0, node.val)
            
        self.preorder(node.left, level+1, ret)
        self.preorder(node.right, level+1, ret)
        
        return
    

