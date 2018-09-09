#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # p.left = parent.right
    # parent.right = p.right
    # p.right = parent
    # parent = p.left
    # p = left
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def upsidedown(p, l):
            if l == None:
                self.root = p
                return p

            upsidedown(l, l.left)
            if p != None:
                l.left = p.right
            else:
                l.left = None
            l.right = p
            return
            
        upsidedown(root, root.left)

        return self.root



class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        parent = None
        right = None

        while node:
            left = node.left
            right = node.right
            node.left = right
            node.right = parent
            parent = node
            node = left

        return parent

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        return self.upsideDownBinaryTreeRecu(root, None)

    def upsideDownBinaryTreeRecu(self, p, parent):
        if p is None:
            return parent

        root = self.upsideDownBinaryTreeRecu(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent

        return root


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None

        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left

        return parent


class Solution(object):
    # p.left = parent.right
    # parent.right = p.right
    # p.right = parent
    # parent = p.left
    # p = left
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # top-down
        node, parent, parentRight = root, None, None
        while node is not None:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left
        return parent
