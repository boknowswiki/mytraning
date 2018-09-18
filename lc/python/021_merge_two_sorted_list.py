#!/usr/bin/python -t

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        ret = ListNode(0)
        head = ret

        while l1 and l2:
            if l1.val < l2.val:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next
            ret = ret.next

        if l1 == None:
            ret.next = l2
        elif l2 == None:
            ret.next = l1

        return head.next

