#!/usr/bin/python -t

# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode()
        prev = dummy

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return dummy.next
    
    
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

