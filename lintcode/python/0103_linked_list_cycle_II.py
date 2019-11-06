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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None
            
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return None
            
            fast = fast.next.next
            slow = slow.next
            
        while head != slow.next:
            head = head.next
            slow = slow.next
            
        return head
        
        
