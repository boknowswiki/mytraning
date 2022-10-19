#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder.pop(0))
        node_index = inorder.index(node.val)
        
        node.left = self.buildTree(preorder, inorder[:node_index])
        node.right = self.buildTree(preorder, inorder[node_index+1:])
        
        return node


class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
            
        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0
        
        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1
        
        return head


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        
        pre = 1
        ino = 0
        while (pre < len(preorder)):
            curr = TreeNode(preorder[pre])
            pre += 1
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino += 1
            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr
                
            stack.append(curr)
        return root
