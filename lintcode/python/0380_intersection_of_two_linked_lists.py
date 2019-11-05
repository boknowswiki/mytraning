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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        ha = headA
        hb = headB
        
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
            
        return ha
        
        
