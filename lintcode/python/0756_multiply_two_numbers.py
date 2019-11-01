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
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        if l1:
            val1 = self.get_val(l1)
        if l2:
            val2 = self.get_val(l2)
        
        return val1 * val2
        
    
    def get_val(self, head):
        if not head:
            return 0
            
        val = 0
        
        while head:
            val = val * 10 + head.val
            head = head.next
            
        return val
        
