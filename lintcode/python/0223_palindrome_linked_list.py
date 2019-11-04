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
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if not head or not head.next:
            return True
            
        mid = self.findMid(head)
        
        l2 = mid.next
        
        tmp = self.reverse(l2)
        
        while head and tmp:
            if head.val != tmp.val:
                return False
                
            head = head.next
            tmp = tmp.next
            
        return tmp == None
            
        
    def findMid(self, head):
        fast = head.next
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
        
    def reverse(self, head):
        if not head or not head.next:
            return head
            
        prev = None
        
        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n
            
        return prev
        
      
