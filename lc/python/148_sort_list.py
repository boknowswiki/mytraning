#!/usr/bin/python -t

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def findmid(head):
            slow = fast = head
            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def merge(h1, h2):
            dummy = ListNode(0)
            prev = dummy
            
            while h1 and h2:
                if h1.val < h2.val:
                    prev.next = h1
                    h1 = h1.next
                else:
                    prev.next = h2
                    h2 = h2.next
                prev = prev.next
                
            if h1:
                prev.next = h1
                
            if h2:
                prev.next = h2
                
            return dummy.next
        
        if head == None or head.next == None:
            return head
        
        mid = findmid(head)
        second = mid.next
        mid.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(second)
        return merge(l1, l2)
