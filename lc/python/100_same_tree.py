#!/usr/bin/python -t

# binary tree and dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        if not q:
            return not p
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return q is None
        if not q:
            return p is None
        
        p_list = self.get_list(p)
        q_list = self.get_list(q)
        
        return p_list == q_list
    
    def get_list(self, node):
        ret = []
        q = collections.deque([node])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    ret.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    ret.append("null")
  
        return ret

#time O(n) space O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None or q == None:
            return p == q
        
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
