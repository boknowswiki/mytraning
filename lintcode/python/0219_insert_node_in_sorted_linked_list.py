#!/usr/bin/python -t

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        if not head:
            return ListNode(val)

        if val < head.val:
            node = ListNode(val)

            node.next = head
            return node

        cur = head

        while cur.next != None and cur.next.val < val:
            cur = cur.next

        next = cur.next
        newNode = ListNode(val)
        cur.next = newNode
        newNode.next = next

        return head
