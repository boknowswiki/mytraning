#!/usr/bin/python -t

# dfs, divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None or root == A or root == B:
            return root
            
        left_node = self.lowestCommonAncestor(root.left, A, B)
        right_node = self.lowestCommonAncestor(root.right, A, B)
        
        if left_node and right_node:
            return root
            
        if left_node:
            return left_node
            
        if right_node:
            return right_node
            
        return None
        

# dfs, lca

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None:
            return None
            
        self.maxd = 0
        self.pmap = {}
        self.imap = {}
        self.dmap = {}
        self.id = 0
        
        self.dfs(root, 0)
        self.parent = [[0] * self.maxd for _ in range(self.id)]
        self.getParent(root)
        
        for i in range(self.id):
            for j in range(1, self.maxd):
                self.parent[i][j] = self.parent[self.parent[i][j-1]][j-1]
                
        if A in self.pmap and B in self.pmap:
            return self.lca(A, B)
        else:
            return None
            
    def lca(self, A, B):
        id_a = self.pmap[A]
        id_b = self.pmap[B]
        if self.dmap[id_a] < self.dmap[id_b]:
            return self.lca(B, A)
            
        for i in range(self.maxd-1, -1, -1):
            if self.dmap[self.parent[id_a][i]] >= self.dmap[id_b]:
                id_a = self.parent[id_a][i]
            if self.dmap[id_a] == self.dmap[id_b]:
                break
                
        if id_a == id_b:
            return self.imap[id_a]
            
        for i in range(self.maxd-1, -1, -1):
            if self.imap[self.parent[id_a][i]] != self.imap[self.parent[id_b][i]]:
                id_a = self.parent[id_a][i]
                id_b = self.parent[id_b][i]
                
        return self.imap[self.parent[id_a][0]]
        
    def getParent(self, node):
        id_node = self.pmap[node]
        if node.left:
            id_left = self.pmap[node.left]
            self.parent[id_left][0] = id_node
            self.getParent(node.left)
            
        if node.right:
            id_right = self.pmap[node.right]
            self.parent[id_right][0] = id_node
            self.getParent(node.right)
            
        
    def dfs(self, node, depth):
        self.pmap[node] = self.id
        self.imap[self.id] = node
        self.dmap[self.id] = depth
        self.maxd = max(self.maxd, depth)
        self.id = self.id + 1
            
        if node.left:
            self.dfs(node.left, depth+1)
        if node.right:
            self.dfs(node.right, depth+1)

