#!/usr/bin/python -t

# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1+v2+carry
            carry = total//10
            node = ListNode(total%10)
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        c = 0

        while l1 or l2:
            val_1 = l1.val if l1 != None else 0
            val_2 = l2.val if l2 != None else 0
            total = val_1 + val_2
            val = (total + c)% 10
            c = (total+c)// 10
            prev.next = ListNode(val=val)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if c:
            prev.next = ListNode(val=c)
            
        return dummy.next

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
