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
    @param head: the head
    @param G: an array
    @return: the number of connected components in G
    """
    def numComponents(self, head, G):
        # Write your code here
        if not head:
            return 0
            
        g = set(G)
        ret = 0
        
        while head:
            if head.val in g and (not head.next or head.next.val not in g):
                ret += 1
                
            head = head.next
            
        return ret
        
        
