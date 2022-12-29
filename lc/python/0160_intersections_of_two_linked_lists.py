
# two pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.

# linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        def get_len(node):
            if not node:
                return 0
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        len_a = get_len(headA)
        len_b = get_len(headB)

        while len_a > len_b:
            headA = headA.next
            len_a -= 1

        while len_b > len_a:
            headB = headB.next
            len_b -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
