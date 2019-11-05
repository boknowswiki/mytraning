#!/usr/bin/python -t

# linked list answer, but no AC.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def inorder(self, node):
        if not node: return
        left = node.left
        for n in self.inorder(left):
            yield n
        yield node
        right = node.right
        for n in self.inorder(right):
            yield n
    
    def treeToDoublyList(self, root):
        # Write your code here.
        if not root: return root
        first = None
        last = None
        prev = None
    	# iterate the tree like a list
        for v in self.inorder(root):
            if first is None: first = v
            last = v
            if prev is not None:
                prev.right = v
                v.left = prev
            prev = v
        first.left = last
        last.right = first
        return first


# linked list, no AC, myself


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        if not root:
            return root
            
        self.first = self.prev = None
        
        self.inorder(root)
        
        self.first.left = self.prev
        self.prev.right = self.first
        
        return self.first
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
        
            if self.first == None:
                self.first = node
            
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            
            self.prev = node
        
            self.inorder(node.right)
        
        return
    
    
