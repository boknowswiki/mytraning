#!/usr/bin/python -t

# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        prev = dummy
        cur = head

        while cur and cur.next:
            nxt = cur.next
            tmp = nxt.next
            prev.next = nxt
            nxt.next = cur
            cur.next = tmp
            prev = cur
            cur = tmp

        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        ret.next = head
        prev = ret
        cur = head

        while cur and cur.next:
            next = cur.next
            tmp = next.next
            prev.next = next
            next.next = cur
            cur.next = tmp
            prev = cur
            cur = tmp

        return ret.next

