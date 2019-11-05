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
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        if not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        
        prev1, prev2 = self.findPrev(dummy, v1, v2)
        
        if not prev1 or not prev2:
            return head
            
        if prev1 == prev2:
            return head
            
        if prev1.next == prev2:
            self.swapCon(prev1)
        elif prev2.next == prev1:
            self.swapCon(prev2)
        else:
            self.swapFar(prev1, prev2)
            
        return dummy.next
        
    def swapCon(self, prev):
        n1 = prev.next
        n2 = n1.next
        post = n2.next
        
        prev.next = n2
        n2.next = n1
        n1.next = post
        
        return
    
    def swapFar(self, prev1, prev2):
        n1 = prev1.next
        p1 = n1.next
        
        n2 = prev2.next
        p2 = n2.next
        
        prev1.next = n2
        n2.next = p1
        
        prev2.next = n1
        n1.next = p2
        
        return
    
        
    def findPrev(self, dummy, v1, v2):
        prev1 = prev2 = None
        
        prev = dummy
        while prev.next:
            if prev.next.val == v1:
                prev1 = prev
            if prev.next.val == v2:
                prev2 = prev
                
            prev = prev.next
            
        return prev1, prev2
        
        
