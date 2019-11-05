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
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if not head:
            return head
            
        r = self.reverse(head)
        
        self.addOne(r)
        
        return self.reverse(r)
        
        
    def reverse(self, head):
        prev = None
        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n
            
        return prev
        
    def addOne(self, l):
        c = 1
        dummy = ListNode(0)
        dummy.next = l
        prev = dummy
        
        while l:
            val = l.val + c
            c = val/10
            val = val%10
            l.val = val
            l = l.next
            prev = prev.next
            
        if c:
            prev.next = ListNode(c)
            
        return
    
