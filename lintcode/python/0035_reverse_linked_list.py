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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        prev = None
        
        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n
            
        return prev
        
