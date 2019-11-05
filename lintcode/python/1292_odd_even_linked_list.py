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
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if not head or not head.next or not head.next.next:
            return head
            
        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd = odd_dummy
        even = even_dummy
        idx = 1
        
        while head:
            if idx % 2:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
                
            head = head.next
            idx += 1
            
        odd.next = even_dummy.next
        even.next = None
        
        return odd_dummy.next
        
        
