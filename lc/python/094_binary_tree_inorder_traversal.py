#!/usr/bin/python -t

# binary tree and dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.helper(root)
        return self.ret
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.ret.append(node.val)
        self.helper(node.right)
        return

# binary tree
# time O(n)
# space O(n) or O(1)

    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
        return res

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        cur = root
        
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
                
        return ret


#time O(n) space worst O(n), average O(nlogn)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, ret):
            if root:
                inorder(root.left, ret)
                ret.append(root.val)
                inorder(root.right, ret)
                
            return
        
        ret = []
        inorder(root, ret)
        
        return ret
