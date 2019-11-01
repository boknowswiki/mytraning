#!/usr/bin/python -t

# linked list, quick sort

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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        mid = self.findMid(head)
        
        left_dummy = ListNode(0)
        mid_dummy = ListNode(0)
        right_dummy = ListNode(0)
        
        left_tail = left_dummy
        mid_tail = mid_dummy
        right_tail = right_dummy
        
        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = left_tail.next
            elif head.val == mid.val:
                mid_tail.next = head
                mid_tail = mid_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
                
            head = head.next
            
        left_tail.next = None
        mid_tail.next = None
        right_tail.next = None
                
        left = self.sortList(left_dummy.next)
        right = self.sortList(right_dummy.next)
        
        return self.concat(left, mid_dummy.next, right)
        
    def concat(self, left, mid, right):
        dummy = ListNode(0)
        prev = dummy
        
        prev.next = left
        prev = self.get_tail(prev)
        prev.next = mid
        prev = self.get_tail(prev)
        prev.next = right
        prev = self.get_tail(prev)
        
        return dummy.next
        
        
    def findMid(self, node):
        if not node:
            return None
        
        fast = node.next
        
        while fast and fast.next:
            fast = fast.next.next
            node = node.next
            
        return node
        
        
    def get_tail(self, node):
        if not node:
            return node
        while node.next:
            node = node.next
            
        return node
        
        


# linked list merge sort

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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
            
        mid = self.findMid(head)
        
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)
        
    
    def merge(self, l, r):
        if not l:
            return r
        if not r:
            return l
            
        dummy = ListNode(0)
        prev = dummy
        
        while l and r:
            if l.val < r.val:
                prev.next = l
                l = l.next
            else:
                prev.next = r
                r = r.next
                
            prev = prev.next
            
        if l:
            prev.next = l
        else:
            prev.next = r
            
        return dummy.next
        
        
    def findMid(self, node):
        if not node:
            return None
        
        fast = node.next
        
        while fast and fast.next:
            fast = fast.next.next
            node = node.next
            
        return node
        
        
