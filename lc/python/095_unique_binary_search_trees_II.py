#!/usr/bin/python -t

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        tree_list = [[[None]] * (n + 2) for i in xrange( n+ 2)]
        for i in xrange(1, n+1):
            tree_list[i][i] = [TreeNode(i)]
            for j in xrange(i-1, 0, -1):
                tree_list[j][i] = []
                for k in xrange(j, i+1):
                    for left in tree_list[j][k-1]:
                        for right in tree_list[k+1][i]:
                            root = TreeNode(k)
                            (root.left, root.right) = (left, right)
                            tree_list[j][i].append(root)
        return tree_list[1][n]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(start, end):
            if start > end:
                return None
            ret = []
            
            for i in range(start, end):
                for l in dfs(start, i) or [None]:
                    for r in dfs(i+1, end) or [None]:
                        node = TreeNode(i)
                        node.left, node.right = l, r
                        ret.append(node)
                        
            return ret
        
        if n == 0:
            return []
        return dfs(1, n+1)
