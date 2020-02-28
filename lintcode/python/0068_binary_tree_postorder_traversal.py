#!/usr/bin/python -t

# binary tree postorder, iteration way


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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        ret = []
        stack = []
        cur = root
        
        while cur:
            stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
                
        while len(stack) != 0:
            cur = stack.pop()
            ret.append(cur.val)
            
            if stack and stack[-1].left == cur:
                cur = stack[-1].right
                while cur:
                    stack.append(cur)
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right
                        
        return ret
        


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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        pre, cur = None, root
        s = [root]
        
        while len(s) > 0:
            cur = s[-1]
            if not pre or pre.left == cur or pre.right == cur:
                if cur.left:
                    s.append(cur.left)
                elif cur.right:
                    s.append(cur.right)
            elif cur.left == pre:
                if cur.right:
                    s.append(cur.right)
            else:
                ret.append(s.pop().val)
                
            pre = cur
        
        return ret

# binary tree postorder, recursive way

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
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
        self.helper(node.right, ret)
        
        ret.append(node.val)
        
        return

