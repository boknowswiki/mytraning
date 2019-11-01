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
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            tmp = head.next.next
            prev.next = head.next
            head.next.next = head
            head.next = tmp
            prev = head
            head = tmp
            
        return dummy.next
        
        
