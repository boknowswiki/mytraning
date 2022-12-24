#!/usr/bin/python -t


# linked list
# time O(n^2)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        dummy = ListNode(float('-inf'))
        prev = dummy

        
        while head:
            while prev.next and prev.next.val < head.val:
                prev = prev.next
             
            prev.next, head.next, head = head, prev.next, head.next

            prev = dummy
        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
            
        dummy = ListNode(0)
        prev = dummy.next = head
        cur = head.next
        
        while cur:
            next = cur.next
            before = dummy
            if cur.val < prev.val:
                while before.next:
                    if before.next.val >= cur.val:
                        prev.next = cur.next
                        before.next, cur.next = cur, before.next
                        break
                    before = before.next
            else:
                prev = cur
            cur = next
            
        return dummy.next

