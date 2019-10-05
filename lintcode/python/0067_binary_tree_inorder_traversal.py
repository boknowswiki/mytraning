#!/usr/bin/python -t

# binary tree traversal inoder, iteration way

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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        cur = root
        s = []
        
        while cur or len(s) > 0:
            while cur:
                s.append(cur)
                cur = cur.left
                
            cur = s.pop()
            ret.append(cur.val)
            cur = cur.right
            
        return ret


# binary tree inorder traversal, recursive way

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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.helper(root, ret)
        
        return ret
        
    def helper(self, node, ret):
        if node == None:
            return
        
        self.helper(node.left, ret)
        ret.append(node.val)
        self.helper(node.right, ret)
        
        return ret

