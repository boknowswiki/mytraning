#!/usr/bin/python -t

# linked list

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        if not node:
            node = ListNode(x)
            node.next = node
            return node
            
        p = node
        prev = None
        
        while True:
            prev = p
            p = p.next
            
            if x <= p.val and x >= prev.val:
                break
            
            if prev.val > p.val and (x < p.val or x > prev.val):
                break
            
            if p is node:
                break
            
        new_node = ListNode(x)
        prev.next = new_node
        new_node.next = p
        
        return new_node
        
      
