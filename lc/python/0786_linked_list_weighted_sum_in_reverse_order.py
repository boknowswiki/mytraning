#!/usr/bin/python -t

# better one

class Solution:
    """
    @param head: the given linked list
    @return:  the weighted sum in reverse order
    """
    def weightedSumReverse(self, head):
        # write your code here
        ans = 0;
        sum = 0;
        while head is not None:
            ans = ans + sum + head.val
            sum = sum + head.val
            head = head.next
        return ans

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
    @param head: the given linked list
    @return:  the weighted sum in reverse order
    """
    def weightedSumReverse(self, head):
        # ListNode -> val: the value of node ,ListNode -> next: the next node of this node
        if not head:
            return 0
            
        l = 0
        
        cur = head
        while cur:
            l += 1
            cur = cur.next
            
        ret = 0
        
        while head:
            ret += head.val * l
            head = head.next
            l -= 1
            
        return ret
        
        
