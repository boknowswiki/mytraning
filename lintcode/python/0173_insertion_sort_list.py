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
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        if not head:
            return head
            
        dummy = ListNode(0)
        
        while head:
            prev = dummy
            
            while prev.next and prev.next.val <= head.val:
                prev = prev.next
            
            tmp = head.next
            head.next = prev.next
            prev.next = head
            head = tmp
            
            
        return dummy.next
        
        
