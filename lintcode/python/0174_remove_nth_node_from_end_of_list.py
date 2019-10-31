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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(n):
            if head == None:
                return head
                
            head = head.next
            
        while head:
            head = head.next
            prev = prev.next
            
        prev.next = prev.next.next
        
        return dummy.next
        
        
