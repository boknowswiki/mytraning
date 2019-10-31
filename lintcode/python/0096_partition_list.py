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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        dummy = ListNode(0)
        less_list = ListNode(0)
        noless_list = ListNode(0)
        dummy.next = less_list
        dummy_2 = ListNode(0)
        dummy_2.next = noless_list
        
        cur = head
        
        while cur:
            if cur.val < x:
                less_list.next = cur
                less_list = less_list.next
            else:
                noless_list.next = cur
                noless_list = noless_list.next
                
            cur = cur.next
            
        noless_list.next = None
        less_list.next = dummy_2.next.next
        
        return dummy.next.next
        
        
