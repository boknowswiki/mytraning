#!/usr/bin/python -t

# linked list
# non-recursive way

"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return None
            
        prev = dummy = DoublyListNode(0, None)
        s = []
        node = root
        
        while len(s) > 0 or node:
            while node:
                s.append(node)
                node = node.left
                
            node = s.pop()
            prev.next = DoublyListNode(node.val, None)
            prev.next.prev = prev
            prev = prev.next
            node = node.right
            
        if dummy.next:
            dummy.next.prev = None
        
        return dummy.next
        

# recursive way
        

"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        dummy = DoublyListNode(0)
        
        self.cur = dummy
        self.helper(root)
        
        return dummy.next 
        
    
    def helper(self, node):
        if node is None:
            return 
        
        self.helper(node.left)
        
        newListNode = DoublyListNode(node.val)
        self.cur.next = newListNode 
        newListNode.prev = self.cur
        self.cur = newListNode

        self.helper(node.right)
            
        return
    
    
