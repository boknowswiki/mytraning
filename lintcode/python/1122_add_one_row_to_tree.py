#!/usr/bin/python -t

# bfs solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def addOneRow(self, root, v, d):
        # write your code here
        st=[(root,1)]
        self.d=d
        if self.d==1:
            newRoot=TreeNode(v)
            newRoot.left=root
            return newRoot
        while st:
            node, lvl=st.pop()
            if lvl==self.d-1:
                temp1=node.left
                temp2=node.right
                node.left=TreeNode(v)
                node.right=TreeNode(v)
                node.left.left=temp1
                node.right.right=temp2
            if node.left:
                st.append((node.left, lvl+1))
            if node.right:
                st.append((node.right, lvl+1))
        return root


# dfs, divid and conquer with traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def addOneRow(self, root, v, d):
        # write your code here
        if not root:
            return None
            
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
            
        if d == 2:
            l_node = TreeNode(v)
            r_node = TreeNode(v)
            root.left, l_node.left = l_node, root.left
            root.right, r_node.right = r_node, root.right
            return root
            
        elif d > 2:
            root.left = self.addOneRow(root.left, v, d-1)
            root.right = self.addOneRow(root.right, v, d-1)
        return root
        
