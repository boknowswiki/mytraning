#!/usr/bin/python -t

# BFS and link list

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

from collections import deque

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
            
        q = deque([root])
        ret = []
        
        while len(q) > 0:
            n = len(q)
            prev = None
            for i in range(n):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                    
                node.next = prev
                prev = node
                
            ret.append(prev)
            
        return ret
        
            
