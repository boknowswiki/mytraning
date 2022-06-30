#!/usr/bin/python -t


# binary tree, iteration way
# time O(n)
# space O(1)

import collections

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []

        queue = collections.deque()
        ret = []

        node = root
        while node is not None:
            queue.append(node)
            node = node.left

        while len(queue) > 0:
            node = queue.pop()
            ret.append(node.val)
            if node.right:
                node = node.right
                while node is not None:
                    queue.append(node)
                    node = node.left

        return ret

# binary tree, divid and conquer way
# time O(n)
# space O(1)


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []

        ret = self.helper(root)

        return ret

    def helper(self, node):
        if not node:
            return []

        ret = self.helper(node.left)
        ret.append(node.val)
        ret.extend(self.helper(node.right))

        return ret

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

