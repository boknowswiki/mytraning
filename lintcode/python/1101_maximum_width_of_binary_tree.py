#!/usr/bin/python -t

# BFS
#这道题目只需要对二叉树进行一次遍历即可. (DFS/BFS都可以)
#
#首先你要明确距离的定义, 是这一层两端的节点在对应的满二叉树中的距离. 我们可以在遍历的过程中维护每个节点在满二叉树的这一层中的下标:
#
#如果一个节点的下标是 idx, 那么它的左子节点的下标就是 idx * 2, 它的右子节点的下标就是 idx * 2 + 1.
#
#我们记录下每一层出现的最大的和最小的下标即可得到这一层的宽度, 然后在所有层的宽度中取最大值即可.
#
#(这道题目节点的 val 属性是没有用的)

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
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        # Write your code here
        q = deque()
        q.append((root, 0, 0))
        cur_depth = left = ret = 0
        
        while len(q) > 0:
            node, depth, pos = q.popleft()
            
            if node:
                q.append((node.left, depth+1, pos*2))
                q.append((node.right, depth+1, pos*2+1))
                
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                    
                ret = max(pos-left+1, ret)
        
        return ret
        
        

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
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        # Write your code here
        if not root:
            return 0
        
        self.ret = 1
        self.level = []
        self.dfs(root, 0, 1)
        
        return self.ret
        
    def dfs(self, node, depth, index):
        if not node:
            return
        
        if len(self.level) == depth:
            self.level.append(index)
            
        self.ret = max(self.ret, index - self.level[depth]+1)
        self.dfs(node.left, depth+1, index*2)
        self.dfs(node.right, depth+1, index*2+1)
        
        return
    
    
