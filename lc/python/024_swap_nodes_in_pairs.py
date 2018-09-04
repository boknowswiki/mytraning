#!/usr/bin/python -t

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

