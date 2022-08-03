#!/usr/bin/python -t


# linked list
# time O(n)
# space O(1)


from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if not head or k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        end = dummy

        while end.next != None:
            for i in range(k):
                if end != None:
                    end = end.next
                else:
                    break
            if end == None:
                break

            start = prev.next
            next = end.next
            end.next = None
            prev.next = self.reverse(start)
            start.next = next
            prev = start
            end = prev

        return dummy.next

    def reverse(self, head):
        if not head or not head.next:
            return head

        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

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
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head or k <= 1:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        while head.next:
            head = self.reverseK(head, k)
            
        return dummy.next
        
    def reverseK(self, head, k):
        k_node = head
        
        for i in range(k):
            if k_node.next == None:
                return k_node
            k_node = k_node.next
            
        first_node = head.next
        prev = head
        cur = first_node
        
        for i in range(k):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
           
        head.next = prev
        first_node.next = cur
        
        return first_node
        
        
