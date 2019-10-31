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
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        if not head:
            return ListNode(val)
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next:
            if prev.next.val > val:
                n = prev.next
                prev.next = ListNode(val)
                prev.next.next = n
                break
            else:
                prev = prev.next
        
        # for val is greater than all of the nodes, insert it to the last one        
        if prev.next == None:
            prev.next = ListNode(val)
            
        return dummy.next
        
       
