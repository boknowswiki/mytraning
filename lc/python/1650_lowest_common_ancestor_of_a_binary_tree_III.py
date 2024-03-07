# dfs
# time O(n)
# space O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = self.get_path(p)

        while q not in p_path:
            q = q.parent

        return q

    def get_path(self, node):
        path = []

        path.append(node)
        while node.parent:
            node = node.parent
            path.append(node)

        return path
        
