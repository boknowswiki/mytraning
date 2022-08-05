#!/usr/bin/python -t

# linked list
# time O(n)
# space O(1)


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        ha = headA
        hb = headB
        
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
            
        return ha
        
        
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None

        lenA = self.get_len(headA)
        lenB = self.get_len(headB)

        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        if headA == headB:
            return headA

        while headA != headB:
            headA = headA.next
            headB = headB.next
            if headA == headB:
                return headA

        return None


    def get_len(self, head):
        cnt = 0

        while head:
            cnt += 1
            head = head.next

        return cnt
