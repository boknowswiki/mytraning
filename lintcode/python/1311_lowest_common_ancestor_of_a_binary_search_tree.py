#!/usr/bin/python -t

# binary tree
# iteration way
# time O(n)
# space O(1)


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if not root:
            return None

        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        s = [root]

        while len(s) != 0:
            node = s.pop()

            if p.val <= node.val <= q.val:
                return node
            elif p.val <= node.val and q.val <= node.val:
                s.append(node.left)
            else:
                s.append(node.right)

        return None

# binary tree
# traversal way
# time O(n)
# space O(1)

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val <= q.val:
            return root
        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)

# dfs, traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if root == None:
            return root
            
        father_v = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > father_v and q_val > father_v:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < father_v and q_val < father_v:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            
