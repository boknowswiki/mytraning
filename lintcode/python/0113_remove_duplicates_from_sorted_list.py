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
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                val = prev.next.val
                while prev.next and prev.next.val == val:
                    prev.next = prev.next.next
                    
            else:
                prev = prev.next
            
        return dummy.next
        
        
