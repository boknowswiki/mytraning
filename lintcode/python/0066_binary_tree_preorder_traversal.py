#!/usr/bin/python -t


# binary tree

# iteration way
# time O(n)
# space O(n)

import collections

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        ret = []
        if not root:
            return ret

        queue = collections.deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop()
            ret.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return ret

# divid and conquer way
# time O(n)
# space O(1)

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []

        return self.helper(root)

    def helper(self, root):
        if not root:
            return []
        ret = [root.val]
        if root.left:
            ret.extend(self.helper(root.left))
        if root.right:
            ret.extend(self.helper(root.right))

        return ret

# traverse way
# time O(n)
# space O(1)


from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        ret = []
        if not root:
            return ret

        self.helper(root, ret)

        return ret

    def helper(self, root, ret):
        ret.append(root.val)
        if root.left:
            self.helper(root.left, ret)
        if root.right:
            self.helper(root.right, ret)

        return

# preorder iteration solution

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        s = [root]
        
        while len(s) > 0:
            node = s.pop()
            ret.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
                
        return ret

# binary tree traversal, recursive way

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.helper(root, ret)
        
        return ret
        
    def helper(self, root, ret):
        if root == None:
            return
        ret.append(root.val)
        self.helper(root.left, ret)
        self.helper(root.right, ret)
        
        return

