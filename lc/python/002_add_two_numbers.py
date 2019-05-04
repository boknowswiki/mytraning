#!/usr/bin/python -t

#time O(max(m,n)) space O(max(m, n)+1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        head = ret
        c = 0

        while l1 and l2:
            sum = l1.val + l2.val + c
            c = sum/10
            rest = sum % 10

            node = ListNode(rest)
            ret.next = node
            ret = ret.next
            l1 = l1.next
            l2 = l2.next

        if l1 == None:
            while l2:
                sum = l2.val + c
                c = sum / 10
                rest = sum % 10
                node = ListNode(rest)
                ret.next = node
                ret = ret.next
                l2 = l2.next
        elif l2 == None:
            while l1:
                sum = l1.val + c
                c = sum / 10
                rest = sum % 10
                node = ListNode(rest)
                ret.next = node
                ret = ret.next
                l1 = l1.next

        if c == 1:
            node = ListNode(c)
            ret.next = node
            ret = ret.next

        return head.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        head = ret
        c = 0

        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c = sum/10
            rest = sum % 10

            node = ListNode(rest)
            ret.next = node
            ret = ret.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if c == 1:
            node = ListNode(c)
            ret.next = node
            ret = ret.next

        return head.next
