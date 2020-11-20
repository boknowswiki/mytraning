#!/usr/bin/python -t

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return head
            
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        l1 = head
        l2 = head
        
        cur = head
        index = 0
        
        while l1 and l1.next and l1.next.next:
            l1 = l1.next.next
            l2 = l2.next
            
        dummy2.next = l2.next
        l2.next = None
        dummy1.next = head

        
        l1 = dummy1.next
        
        print "l1"
        while l1:
            print l1.val
            l1 = l1.next
            
        print "l2"
        l2 = dummy2.next
        while l2:
            print l2.val
            l2 = l2.next
            

        dummy2.next = self.reverse(dummy2.next)
        
        print "l2 reverse"
        l2 = dummy2.next
        while l2:
            print l2.val
            l2 = l2.next
            
        dummy = ListNode(0)
        prev = dummy
        
        index = 0
        l1 = dummy1.next
        l2 = dummy2.next
        
        while l1 or l2:
            if index % 2 == 0:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            index += 1
            prev = prev.next
            
        return dummy.next
        
    def reverse(self, node):
        if not node:
            return node
            
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
            
        return prev
            
