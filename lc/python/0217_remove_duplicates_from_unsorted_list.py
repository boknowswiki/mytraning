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
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        if not head:
            return head
            
        v = set()
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next:
            if cur.next.val not in v:
                v.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
            
        return dummy.next
        
        
        
