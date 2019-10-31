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
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1
            
        dummy = ListNode(0)
        prev = dummy
        c = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = (val1+val2+c)%10
            c = (val1+val2+c)/10
            prev.next = ListNode(val)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if c:
            prev.next = ListNode(c)
                
        return dummy.next
        
    
