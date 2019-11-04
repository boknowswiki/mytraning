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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head or not head.next:
            return head
            
        if k == 0:
            return head
            
        length = 0
        
            
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        
        while head:
            head = head.next
            length += 1
            
        head = prev
        k = k%length
        
        for _ in range(k):
            if head == None:
                return dummy.next
                
            head = head.next

        while head.next:
            head = head.next
            prev = prev.next
            
        head.next = dummy.next
        head = prev.next
        prev.next = None
        
        return head
        

