#!/usr/bin/python -t

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2lists(l1, l2):
            ret = ListNode(0)
            head = ret

            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next

                head = head.next

            if l1 == None:
                head.next = l2
            elif l2 == None:
                head.next = l1

            return ret.next

        n = len(lists)
        if n == 0:
            return None
        end = n - 1

        while end > 0:
            start = 0

            while start < end:
                lists[start] = merge2lists(lists[start], lists[end])
                start = start + 1
                end = end - 1

        return lists[0]

